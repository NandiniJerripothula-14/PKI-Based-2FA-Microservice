from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import base64
import os
import time
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import pyotp

DATA_DIR = "/data"
SEED_PATH = os.path.join(DATA_DIR, "seed.txt")
PRIVATE_KEY_PATH = "student_private.pem"

app = FastAPI()


class EncryptedSeedRequest(BaseModel):
    encrypted_seed: str


class VerifyRequest(BaseModel):
    code: Optional[str]


def load_private_key(path: str):
    with open(path, "rb") as f:
        pem = f.read()
    return serialization.load_pem_private_key(pem, password=None)


def decrypt_seed(encrypted_seed_b64: str, private_key) -> str:
    try:
        ct = base64.b64decode(encrypted_seed_b64)
        pt = private_key.decrypt(
            ct,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        hex_seed = pt.decode("utf-8").strip()
        if len(hex_seed) != 64 or any(c not in "0123456789abcdef" for c in hex_seed.lower()):
            raise ValueError("Invalid seed format")
        return hex_seed.lower()
    except Exception:
        raise


def hex_to_base32(hex_seed: str) -> str:
    b = bytes.fromhex(hex_seed)
    return base64.b32encode(b).decode("utf-8")


def generate_totp_code(hex_seed: str) -> str:
    base32 = hex_to_base32(hex_seed)
    totp = pyotp.TOTP(base32, digits=6, interval=30)
    return totp.now()


def verify_totp(hex_seed: str, code: str, window: int = 1) -> bool:
    base32 = hex_to_base32(hex_seed)
    totp = pyotp.TOTP(base32, digits=6, interval=30)
    try:
        return totp.verify(code, valid_window=window)
    except Exception:
        return False


@app.post("/decrypt-seed")
def api_decrypt_seed(req: EncryptedSeedRequest):
    try:
        private_key = load_private_key(PRIVATE_KEY_PATH)
    except Exception:
        raise HTTPException(status_code=500, detail={"error": "Private key load failed"})

    try:
        hex_seed = decrypt_seed(req.encrypted_seed, private_key)
    except Exception:
        raise HTTPException(status_code=500, detail={"error": "Decryption failed"})

    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(SEED_PATH, "w", newline="\n") as f:
            f.write(hex_seed)
        os.chmod(SEED_PATH, 0o600)
    except Exception:
        raise HTTPException(status_code=500, detail={"error": "Failed to save seed"})

    return {"status": "ok"}


@app.get("/generate-2fa")
def api_generate_2fa():
    if not os.path.exists(SEED_PATH):
        raise HTTPException(status_code=500, detail={"error": "Seed not decrypted yet"})
    try:
        with open(SEED_PATH, "r") as f:
            hex_seed = f.read().strip()
        code = generate_totp_code(hex_seed)
        period = 30
        now = int(time.time())
        valid_for = period - (now % period)
        if valid_for == 0:
            valid_for = period
        return {"code": code, "valid_for": valid_for}
    except Exception:
        raise HTTPException(status_code=500, detail={"error": "Seed not decrypted yet"})


@app.post("/verify-2fa")
def api_verify_2fa(req: VerifyRequest):
    if not req.code:
        return JSONResponse(status_code=400, content={"error": "Missing code"})
    if not os.path.exists(SEED_PATH):
        raise HTTPException(status_code=500, detail={"error": "Seed not decrypted yet"})
    try:
        with open(SEED_PATH, "r") as f:
            hex_seed = f.read().strip()
        valid = verify_totp(hex_seed, req.code, window=1)
        return {"valid": bool(valid)}
    except Exception:
        raise HTTPException(status_code=500, detail={"error": "Seed not decrypted yet"})


@app.get("/health")
def health():
    return {"status": "ok"}
