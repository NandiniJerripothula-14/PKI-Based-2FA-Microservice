# QUICK SUBMISSION REFERENCE

## Copy-Paste These Values

### Commit Hash
```
b8d5a0c99613e815ee84962bd7bbf580f184d0ae
```

### Repository URL
```
https://github.com/NandiniJerripothula-14/PKI-Based-2FA-MicroService
```

### Student ID
```
23mh1a42e7
```

### Encrypted Seed (copy from encrypted_seed.txt)
```
hwpWnckygyMyQzaXdpM8/3ae7ImRFQThP7e84oroiiuAIuYCI1czK/Vdu/w/OWfV4D0hD2hjPWLh6QfZssIfVTa3Fz4zcWIoIkUmbt10fFsTr3YEcXeICOV1Revp9ch/SUnOI4KVgQQVO5JoaLhDARM4o+16BR9Ft58hmyqeZrI/gHv4AR78H+Y5IeW/ZhuM0ykh/QSCJeibPjQkw/Xra13U50iGA5/3k8oUC8rMGghSNOea9uMi+8VoFzd+HQbDa2Z5nW0pbSFmnIu4cloDONUqoraOYCSEkQuyPGE026a1hT1r8j2QzzQ4Z8MgT0/Z5j5gqn2vrVZaX/NbS99XvkudPupiS1l05UP58QYWS6lZTI5mYhTEVLNrX6uwy90aDSqRnA9T/VqeEpXEpop3zSJ+1YpbCDOvskibUuA0KHtJvcqMfqzaIGswyvpkj8lpAE9Y0o9FWUBZZqAfBzjtRu3c+aYaJ8uRYNJk76GsyljEGARqU5CGr4H8COclF3faIihhJ575LqHQ6NHvSxhRq2ct9qVmlqt/iVo+1mA8d61WjlMh6nQ+oVdKz5H+xX2xhkuxTMMLSn38DUulzBJ7+JGzDITFzDbVrLzpUEK8aA8xa8TQjTj51hmzWODhl2SBcjaJRaGig/97PiD3cSfaedLgVMvILJSgiUzrbB4Tgso=
```

### Student Public Key (from student_public.pem)
```
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAppAKkvKuN06VebJPAakWBi8T7tWdPJjguxMh125Y9Zc5vYsoAhWwnKu6i32TeOIJP5XiporrIwWf3jLw/aVLpodWzJ6+JWTV+RfbkPREmzTKOjehF431twPs1NHzqJORFnky118ECquqCGdHV6Cac3mE3+OgYIKTPAfsk9K3uMTnJP19OOhBBPo+BeIDC529pYh3ch62U6viEsMOM0m4sM72PO1RC93AJySgRqsVPEWPEJ8OQOsT0hlQFEvtgcRTjBFCtdhT89D7TGnYqqrFPsQ5S6hOTKFh/UBt4znDzFzZTiUvTkv3V0mJWZMtslZkGNunCqI/5kdeZ214f371ZSWwvp6orqFVvjZ3ZI4uOZF77zC+K5ukN84zpx4+BInwom7oBmXmgMNVknpk9dmRC+MK9pPcCwLEhXJP1wzrySnI8pOLLMFmxk663RShwocJbLpdCYG/gB6+FCPfrh0sSF9JwFnrrpzGJHU3TKcz5VlPdZuTxKlhqijO6YuNjdCTPiQaZrKBPba3qDoqlEKiaHjP1dmjJBmZY7kWxrRb4ElpZkB3ZLCcam6/XBMQlIUy27QQAbAAENcetCmH8gEu1O9bxi8Aj1b3Y/PGS7h3/9/WLv2F59AaCAnvwWomihnnmGezFqdFN3x7sEUBMiHprCq39ezzJNLkhcvkQb+pYdsCAwEAAQ==
-----END PUBLIC KEY-----
```

---

## What Still Needs Instructor Key

**Encrypted Commit Signature:**
1. Obtain the real `instructor_public.pem` from course materials
2. Replace the placeholder file
3. Run: `python generate_final_proof.py`
4. Copy the "Encrypted Signature (base64, single line)" output

This is the only value not yet available - everything else is ready.

---

## Final Verification Commands

```bash
# Check everything is committed
git status

# Verify commit hash
git log -1 --format=%H

# Test API locally
python test_endpoints.py

# Check Docker is running
docker ps --filter name=pki-2fa-app

# Verify health endpoint
curl http://localhost:8080/health

# Check cron logs (wait 70+ seconds after startup)
docker exec pki-2fa-app tail -n 5 /cron/last_code.txt
```

All should return success/OK responses.

---

## Files Created for Submission

All files are in your Git repository:
- `SUBMISSION_FORM.md` — Complete form template with all values
- `SUBMISSION_CHECKLIST.md` — Detailed checklist of all features
- `SUBMISSION_VALUES.md` — Quick reference of key information
- `SUBMISSION_REFERENCE.md` ← You are here

Pull these files from your repository when ready to submit.
