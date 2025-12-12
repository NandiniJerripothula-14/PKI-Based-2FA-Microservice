#!/usr/bin/env python3
import subprocess
import base64
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

STUDENT_KEY = "student_private.pem"
INSTRUCTOR_KEY = "instructor_public.pem"


def get_commit_hash():
    out = subprocess.check_output(["git", "log", "-1", "--format=%H"]).strip()
    return out.decode('utf-8')


def load_private_key(path):
    with open(path, 'rb') as f:
        return serialization.load_pem_private_key(f.read(), password=None)


def load_public_key(path):
    with open(path, 'rb') as f:
        return serialization.load_pem_public_key(f.read())


def sign_message(message: str, private_key) -> bytes:
    return private_key.sign(
        message.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )


def encrypt_with_public_key(data: bytes, public_key) -> bytes:
    return public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def main():
    commit = get_commit_hash()
    priv = load_private_key(STUDENT_KEY)
    sig = sign_message(commit, priv)
    pub = load_public_key(INSTRUCTOR_KEY)
    enc = encrypt_with_public_key(sig, pub)
    b64 = base64.b64encode(enc).decode('utf-8')
    print("Commit Hash:", commit)
    print("Encrypted Signature (base64):")
    print(b64)


if __name__ == '__main__':
    main()
