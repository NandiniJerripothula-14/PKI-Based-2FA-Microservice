#!/usr/bin/env python3
"""Generate commit proof: sign commit hash with student private key, encrypt with instructor public key."""
import subprocess
import base64
import sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def generate_proof():
    """Generate signed and encrypted proof of commit."""
    
    # Get commit hash
    try:
        out = subprocess.check_output(["git", "log", "-1", "--format=%H"], cwd=".")
        commit_hash = out.strip().decode('utf-8')
        print(f"✅ Commit Hash: {commit_hash}")
    except Exception as e:
        print(f"❌ Failed to get commit hash: {e}")
        return False
    
    # Load student private key
    try:
        with open('student_private.pem', 'rb') as f:
            private_key = serialization.load_pem_private_key(f.read(), password=None)
        print(f"✅ Loaded student private key")
    except Exception as e:
        print(f"❌ Failed to load student private key: {e}")
        return False
    
    # Sign commit hash with RSA-PSS-SHA256
    try:
        signature = private_key.sign(
            commit_hash.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        print(f"✅ Signed commit hash with RSA-PSS-SHA256")
        print(f"   Signature length: {len(signature)} bytes")
    except Exception as e:
        print(f"❌ Failed to sign: {e}")
        return False
    
    # Check if instructor public key exists and is valid
    try:
        with open('instructor_public.pem', 'rb') as f:
            key_content = f.read()
        
        # Try to parse it
        try:
            instructor_key = serialization.load_pem_public_key(key_content)
            print(f"✅ Loaded instructor public key")
            
            # Encrypt signature with instructor public key
            encrypted_signature = instructor_key.encrypt(
                signature,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            print(f"✅ Encrypted signature with instructor public key (RSA/OAEP-SHA256)")
            print(f"   Encrypted signature length: {len(encrypted_signature)} bytes")
            
            # Base64 encode
            encrypted_b64 = base64.b64encode(encrypted_signature).decode('utf-8')
            
            print(f"\n{'='*70}")
            print(f"PROOF OF WORK GENERATED")
            print(f"{'='*70}")
            print(f"\nCommit Hash (40 chars):\n{commit_hash}")
            print(f"\nEncrypted Signature (base64, single line):\n{encrypted_b64}")
            print(f"\n{'='*70}")
            print(f"\nIMPORTANT NOTES:")
            print(f"  - Commit hash is 40 characters (40-char hex string)")
            print(f"  - Encrypted signature is a single line (no line breaks)")
            print(f"  - Both must be submitted exactly as shown above")
            print(f"\n{'='*70}")
            
            return True
            
        except Exception as e:
            print(f"⚠️  Instructor public key is invalid/placeholder: {e}")
            print(f"    This is expected for testing purposes.")
            print(f"\n    SUBSTITUTE STEPS WHEN YOU HAVE REAL INSTRUCTOR KEY:")
            print(f"    1. Replace instructor_public.pem with the real public key")
            print(f"    2. Re-run this script to generate the encrypted proof")
            print(f"    3. Submit the commit hash and encrypted signature")
            print(f"\nCOMMIT HASH (for submission when real key is available):")
            print(f"{commit_hash}")
            return True
            
    except Exception as e:
        print(f"❌ Failed to load instructor public key: {e}")
        return False

if __name__ == '__main__':
    success = generate_proof()
    sys.exit(0 if success else 1)
