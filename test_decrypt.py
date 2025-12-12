#!/usr/bin/env python3
"""Test seed decryption before container deployment."""
import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def test_decrypt():
    """Test decryption of seed."""
    with open('student_private.pem', 'rb') as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
    
    with open('encrypted_seed.txt', 'r') as f:
        encrypted_b64 = f.read().strip()
    
    print("Testing seed decryption...")
    try:
        ct = base64.b64decode(encrypted_b64)
        pt = private_key.decrypt(
            ct,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        hex_seed = pt.decode("utf-8").strip()
        
        if len(hex_seed) == 64 and all(c in '0123456789abcdef' for c in hex_seed.lower()):
            print(f"✅ Decryption successful!")
            print(f"Hex Seed (64 chars): {hex_seed}")
            return hex_seed
        else:
            print(f"❌ Invalid seed format: {hex_seed}")
            return None
    except Exception as e:
        print(f"❌ Decryption failed: {e}")
        return None

if __name__ == '__main__':
    test_decrypt()
