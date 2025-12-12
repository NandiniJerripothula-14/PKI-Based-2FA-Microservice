#!/usr/bin/env python3
"""Request encrypted seed from instructor API."""
import requests
import json

STUDENT_ID = "23mh1a42e7"
GITHUB_REPO_URL = "https://github.com/NandiniJerripothula-14/PKI-Based-2FA-MicroService"
API_URL = "https://eajeyq4r3zljoq4rpovy2nthda0vtjqf.lambda-url.ap-south-1.on.aws"

def request_seed():
    """Request encrypted seed from instructor API."""
    # Read public key
    with open('student_public.pem', 'r') as f:
        public_key = f.read()
    
    payload = {
        "student_id": STUDENT_ID,
        "github_repo_url": GITHUB_REPO_URL,
        "public_key": public_key
    }
    
    print("Requesting encrypted seed from instructor API...")
    print(f"Student ID: {STUDENT_ID}")
    print(f"GitHub Repo: {GITHUB_REPO_URL}")
    
    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('status') == 'success':
            encrypted_seed = data.get('encrypted_seed')
            print(f"\n✅ Encrypted seed received!")
            
            # Save to file
            with open('encrypted_seed.txt', 'w') as f:
                f.write(encrypted_seed)
            
            print(f"Saved to: encrypted_seed.txt")
            print(f"\nEncrypted Seed (base64):\n{encrypted_seed}")
            return encrypted_seed
        else:
            print(f"❌ API Error: {data}")
            return None
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None

if __name__ == '__main__':
    request_seed()
