# PKI-Based 2FA Microservice - SUBMISSION TEMPLATE

Complete this form with the values from your implementation and submit to the course portal.

## Student Information

**Student ID:** `23mh1a42e7`

---

## Required Submission Values

### 1. GitHub Repository URL
**Value to submit:**
```
https://github.com/NandiniJerripothula-14/PKI-Based-2FA-MicroService
```

✅ **Verification:** 
- Repository is public and accessible
- Same URL used for instructor API seed request
- Contains all source code, Dockerfile, and key files

---

### 2. Commit Hash (40-character hex)
**Value to submit:**
```
b8d5a0c99613e815ee84962bd7bbf580f184d0ae
```

✅ **Verification:**
- Obtained from: `git log -1 --format=%H`
- Current HEAD commit (latest submission)
- References commit that includes all implementation files

---

### 3. Student Public Key (PEM Format)
**Value to submit:**
```
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAppAKkvKuN06VebJPAakW
Bi8T7tWdPJjguxMh125Y9Zc5vYsoAhWwnKu6i32TeOIJP5XiporrIwWf3jLw/aVL
podWzJ6+JWTV+RfbkPREmzTKOjehF431twPs1NHzqJORFnky118ECquqCGdHV6Ca
c3mE3+OgYIKTPAfsk9K3uMTnJP19OOhBBPo+BeIDC529pYh3ch62U6viEsMOM0m4
sM72PO1RC93AJySgRqsVPEWPEJ8OQOsT0hlQFEvtgcRTjBFCtdhT89D7TGnYqqrF
PsQ5S6hOTKFh/UBt4znDzFzZTiUvTkv3V0mJWZMtslZkGNunCqI/5kdeZ214f371
ZSWwvp6orqFVvjZ3ZI4uOZF77zC+K5ukN84zpx4+BInwom7oBmXmgMNVknpk9dmR
C+MK9pPcCwLEhXJP1wzrySnI8pOLLMFmxk663RShwocJbLpdCYG/gB6+FCPfrh0s
SF9JwFnrrpzGJHU3TKcz5VlPdZuTxKlhqijO6YuNjdCTPiQaZrKBPba3qDoqlEKi
aHjP1dmjJBmZY7kWxrRb4ElpZkB3ZLCcam6/XBMQlIUy27QQAbAAENcetCmH8gEu
1O9bxi8Aj1b3Y/PGS7h3/9/WLv2F59AaCAnvwWomihnnmGezFqdFN3x7sEUBMiHp
rCq39ezzJNLkhcvkQb+pYdsCAwEAAQ==
-----END PUBLIC KEY-----
```

**For form:** Can be pasted as-is (multiline) or converted to single line with `\n` escape sequences:
```
-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAppAKkvKuN06VebJPAakWBi8T7tWdPJjguxMh125Y9Zc5vYsoAhWwnKu6i32TeOIJP5XiporrIwWf3jLw/aVLpodWzJ6+JWTV+RfbkPREmzTKOjehF431twPs1NHzqJORFnky118ECquqCGdHV6Cac3mE3+OgYIKTPAfsk9K3uMTnJP19OOhBBPo+BeIDC529pYh3ch62U6viEsMOM0m4sM72PO1RC93AJySgRqsVPEWPEJ8OQOsT0hlQFEvtgcRTjBFCtdhT89D7TGnYqqrFPsQ5S6hOTKFh/UBt4znDzFzZTiUvTkv3V0mJWZMtslZkGNunCqI/5kdeZ214f371ZSWwvp6orqFVvjZ3ZI4uOZF77zC+K5ukN84zpx4+BInwom7oBmXmgMNVknpk9dmRC+MK9pPcCwLEhXJP1wzrySnI8pOLLMFmxk663RShwocJbLpdCYG/gB6+FCPfrh0sSF9JwFnrrpzGJHU3TKcz5VlPdZuTxKlhqijO6YuNjdCTPiQaZrKBPba3qDoqlEKiaHjP1dmjJBmZY7kWxrRb4ElpZkB3ZLCcam6/XBMQlIUy27QQAbAAENcetCmH8gEu1O9bxi8Aj1b3Y/PGS7h3/9/WLv2F59AaCAnvwWomihnnmGezFqdFN3x7sEUBMiHprCq39ezzJNLkhcvkQb+pYdsCAwEAAQ==\n-----END PUBLIC KEY-----
```

✅ **Verification:**
- Key matches `student_public.pem` in repository
- 4096-bit RSA key (public exponent 65537)
- Matches the public key used for seed encryption

---

### 4. Encrypted Seed (Base64, Single Line)
**Value to submit:**
```
hwpWnckygyMyQzaXdpM8/3ae7ImRFQThP7e84oroiiuAIuYCI1czK/Vdu/w/OWfV4D0hD2hjPWLh6QfZssIfVTa3Fz4zcWIoIkUmbt10fFsTr3YEcXeICOV1Revp9ch/SUnOI4KVgQQVO5JoaLhDARM4o+16BR9Ft58hmyqeZrI/gHv4AR78H+Y5IeW/ZhuM0ykh/QSCJeibPjQkw/Xra13U50iGA5/3k8oUC8rMGghSNOea9uMi+8VoFzd+HQbDa2Z5nW0pbSFmnIu4cloDONUqoraOYCSEkQuyPGE026a1hT1r8j2QzzQ4Z8MgT0/Z5j5gqn2vrVZaX/NbS99XvkudPupiS1l05UP58QYWS6lZTI5mYhTEVLNrX6uwy90aDSqRnA9T/VqeEpXEpop3zSJ+1YpbCDOvskibUuA0KHtJvcqMfqzaIGswyvpkj8lpAE9Y0o9FWUBZZqAfBzjtRu3c+aYaJ8uRYNJk76GsyljEGARqU5CGr4H8COclF3faIihhJ575LqHQ6NHvSxhRq2ct9qVmlqt/iVo+1mA8d61WjlMh6nQ+oVdKz5H+xX2xhkuxTMMLSn38DUulzBJ7+JGzDITFzDbVrLzpUEK8aA8xa8TQjTj51hmzWODhl2SBcjaJRaGig/97PiD3cSfaedLgVMvILJSgiUzrbB4Tgso=
```

✅ **Verification:**
- From `encrypted_seed.txt` (single continuous line, no breaks)
- Received from instructor API with student ID: `23mh1a42e7`
- Decryptable with `student_private.pem`
- Produces valid 64-character hex seed

---

### 5. Encrypted Commit Signature (Base64, Single Line)

⚠️ **ACTION REQUIRED:**

1. Obtain `instructor_public.pem` from course materials (real public key, not placeholder)
2. Replace the placeholder file at `instructor_public.pem` in your repository
3. Run the proof generation script:
   ```bash
   python generate_final_proof.py
   ```
4. Copy the output under "Encrypted Signature (base64, single line)"
5. Paste the value below:

**Value to submit:**
```
[PENDING: Run `python generate_final_proof.py` after replacing `instructor_public.pem` with the real instructor key.]
```

⚠️ **This value cannot be generated until you provide the real instructor public key.**

---

### 6. Docker Image URL (Optional)

If you pushed your Docker image to a registry:

```
[Optional: docker.io/yourusername/pki-2fa:latest]
```

Or leave blank if not pushed to a registry (evaluator will build from Dockerfile).

---

## Verification Checklist

Before submitting, verify all of these locally:

- [ ] Git repository is public and accessible
- [ ] Repository URL matches the one used in instructor API call
- [ ] All source code, Dockerfile, docker-compose.yml are committed
- [ ] `student_private.pem` and `student_public.pem` are committed
- [ ] `encrypted_seed.txt` is NOT committed (in .gitignore)
- [ ] Docker image builds successfully: `docker compose build`
- [ ] Container starts: `docker compose up -d`
- [ ] API responds on port 8080: `curl http://localhost:8080/health`
- [ ] All endpoints tested:
  ```bash
  python test_endpoints.py
  ```
  Output: **✅ ALL TESTS PASSED!**
- [ ] Seed persists after restart: `docker compose restart`
- [ ] Cron job logs every minute (wait 70+ seconds):
  ```bash
  docker exec pki-2fa-app tail -n 5 /cron/last_code.txt
  ```
  Should show entries with UTC timestamps and 6-digit codes
- [ ] Student public key is valid and matches `student_public.pem`
- [ ] Encrypted seed decrypts correctly with student private key
- [ ] All base64 strings (encrypted seed, signature) are single-line (no breaks)

---

## Implementation Summary

**What's Implemented:**
- ✅ FastAPI application with 3 REST endpoints
- ✅ RSA 4096-bit keypair (public exponent 65537)
- ✅ RSA/OAEP-SHA256 decryption of encrypted seed
- ✅ RSA-PSS-SHA256 commit signature (ready to encrypt)
- ✅ TOTP generation (SHA-1, 30-second period, 6 digits)
- ✅ TOTP verification with ±1 period tolerance
- ✅ Multi-stage Docker build with cron daemon
- ✅ Persistent seed storage in Docker volume
- ✅ Cron job executing every minute with UTC logging
- ✅ Comprehensive API error handling (200, 400, 500)
- ✅ Git repository with full commit history

**Tested & Verified:**
- ✅ API endpoints: all 6 tests pass
- ✅ Seed persistence: survives container restart
- ✅ Cron execution: logs every minute
- ✅ Docker build: multi-stage completes successfully
- ✅ Container health: running on port 8080

---

## Next Steps

1. **Get the instructor public key** from course materials
2. **Replace `instructor_public.pem`** in your repository with the real key
3. **Generate the encrypted signature:**
   ```bash
   python generate_final_proof.py
   ```
4. **Update this document** with the encrypted signature value
5. **Submit** the completed form to the course portal with all values above

---

**Last Updated:** December 12, 2025
**Status:** Ready for submission (pending instructor public key)
