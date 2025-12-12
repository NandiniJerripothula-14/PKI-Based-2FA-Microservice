# PKI-Based 2FA Microservice

This microservice implements RSA/OAEP decryption of an instructor-provided encrypted seed, TOTP generation and verification (6 digits, SHA-1, 30s), and a cron job that logs codes every minute to `/cron/last_code.txt` (UTC).

Key files `student_private.pem`, `student_public.pem`, and `instructor_public.pem` are included in the repository (required for assignment). The decrypted seed is persisted in the Docker volume at `/data/seed.txt`.

Build and run:

```bash
docker compose build
docker compose up -d
```

API endpoints (port 8080):
- POST /decrypt-seed {"encrypted_seed": "BASE64"}
- GET /generate-2fa -> {"code":"123456","valid_for":30}
- POST /verify-2fa {"code":"123456"}
- GET /health -> {"status":"ok"}
