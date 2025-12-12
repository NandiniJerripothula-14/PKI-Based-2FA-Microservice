#!/usr/bin/env python3
"""Test all API endpoints."""
import requests
import json
import time

BASE_URL = "http://localhost:8080"

def test_health():
    """Test /health endpoint."""
    print("\n=== Test 1: /health ===")
    try:
        resp = requests.get(f"{BASE_URL}/health", timeout=5)
        print(f"Status: {resp.status_code}")
        print(f"Response: {resp.json()}")
        return resp.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_decrypt_seed():
    """Test /decrypt-seed endpoint."""
    print("\n=== Test 2: /decrypt-seed ===")
    try:
        with open('encrypted_seed.txt', 'r') as f:
            encrypted = f.read().strip()
        
        resp = requests.post(
            f"{BASE_URL}/decrypt-seed",
            json={"encrypted_seed": encrypted},
            timeout=5
        )
        print(f"Status: {resp.status_code}")
        print(f"Response: {resp.json()}")
        return resp.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_generate_2fa():
    """Test /generate-2fa endpoint."""
    print("\n=== Test 3: /generate-2fa ===")
    try:
        resp = requests.get(f"{BASE_URL}/generate-2fa", timeout=5)
        print(f"Status: {resp.status_code}")
        data = resp.json()
        print(f"Response: {data}")
        
        if resp.status_code == 200:
            code = data.get('code')
            valid_for = data.get('valid_for')
            print(f"✅ Generated code: {code}, valid for {valid_for}s")
            return code
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def test_verify_2fa(code):
    """Test /verify-2fa endpoint with valid code."""
    print("\n=== Test 4: /verify-2fa (valid code) ===")
    try:
        resp = requests.post(
            f"{BASE_URL}/verify-2fa",
            json={"code": code},
            timeout=5
        )
        print(f"Status: {resp.status_code}")
        data = resp.json()
        print(f"Response: {data}")
        
        if resp.status_code == 200 and data.get('valid'):
            print(f"✅ Code verified successfully!")
            return True
        else:
            print(f"❌ Code verification failed")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_verify_invalid_code():
    """Test /verify-2fa endpoint with invalid code."""
    print("\n=== Test 5: /verify-2fa (invalid code) ===")
    try:
        resp = requests.post(
            f"{BASE_URL}/verify-2fa",
            json={"code": "000000"},
            timeout=5
        )
        print(f"Status: {resp.status_code}")
        data = resp.json()
        print(f"Response: {data}")
        
        if resp.status_code == 200 and not data.get('valid'):
            print(f"✅ Invalid code correctly rejected")
            return True
        else:
            print(f"❌ Unexpected response")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_verify_missing_code():
    """Test /verify-2fa endpoint with missing code."""
    print("\n=== Test 6: /verify-2fa (missing code) ===")
    try:
        resp = requests.post(
            f"{BASE_URL}/verify-2fa",
            json={},
            timeout=5
        )
        print(f"Status: {resp.status_code}")
        data = resp.json()
        print(f"Response: {data}")
        
        if resp.status_code == 400 and data.get('error') == 'Missing code':
            print(f"✅ Missing code correctly rejected with 400")
            return True
        else:
            print(f"❌ Unexpected response")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("API ENDPOINT TESTS")
    print("=" * 60)
    
    results = []
    
    # Test health
    results.append(("Health check", test_health()))
    
    # Test decrypt
    results.append(("Decrypt seed", test_decrypt_seed()))
    
    # Test generate
    code = test_generate_2fa()
    results.append(("Generate 2FA", code is not None))
    
    if code:
        # Test verify valid
        results.append(("Verify valid code", test_verify_2fa(code)))
    
    # Test verify invalid
    results.append(("Verify invalid code", test_verify_invalid_code()))
    
    # Test verify missing
    results.append(("Verify missing code", test_verify_missing_code()))
    
    print("\n" + "=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {name}")
    
    all_passed = all(p for _, p in results)
    print("=" * 60)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED")
    
    return all_passed

if __name__ == '__main__':
    main()
