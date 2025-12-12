#!/usr/bin/env python3
"""Generate 4096-bit RSA keypair and save to PEM files."""
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keypair():
    """Generate 4096-bit RSA keypair."""
    print("Generating 4096-bit RSA keypair...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
    )
    public_key = private_key.public_key()
    
    # Serialize to PEM
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode('utf-8')
    
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode('utf-8')
    
    # Save to files
    with open('student_private.pem', 'w') as f:
        f.write(private_pem)
    
    with open('student_public.pem', 'w') as f:
        f.write(public_pem)
    
    print("✅ Keypair generated and saved:")
    print("   - student_private.pem")
    print("   - student_public.pem")
    print(f"\nPublic Key:\n{public_pem}")
    return public_pem

if __name__ == '__main__':
    generate_keypair()
