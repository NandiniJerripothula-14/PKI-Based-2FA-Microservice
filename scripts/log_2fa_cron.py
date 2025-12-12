#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime
import base64
import pyotp

SEED_PATH = "/data/seed.txt"


def hex_to_base32(hex_seed: str) -> str:
    b = bytes.fromhex(hex_seed)
    return base64.b32encode(b).decode("utf-8")


def main():
    try:
        if not os.path.exists(SEED_PATH):
            print(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} - Seed missing", file=sys.stderr)
            return
        with open(SEED_PATH, "r") as f:
            hex_seed = f.read().strip()
        base32 = hex_to_base32(hex_seed)
        totp = pyotp.TOTP(base32, digits=6, interval=30)
        code = totp.now()
        ts = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        print(f"{ts} - 2FA Code: {code}")
    except Exception as e:
        print(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} - Error: {e}", file=sys.stderr)


if __name__ == '__main__':
    main()
