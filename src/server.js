// src/server.js
require('dotenv').config();

const express = require('express');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { authenticator } = require('otplib');
const base32 = require('hi-base32');

// --- Config ---
const app = express();
const PORT = process.env.PORT || 8080;
const DATA_DIR = process.env.DATA_DIR || '/data';
const SEED_FILE = path.join(DATA_DIR, 'seed.txt');
const STUDENT_PRIVATE_KEY_PATH =
  process.env.STUDENT_PRIVATE_KEY_PATH || path.join(__dirname, '../student_private.pem');

// Configure otplib for TOTP (SHA1, 30s period, 6 digits)
authenticator.options = {
  step: 30,
  digits: 6,
  algorithm: 'sha1',
};

app.use(express.json());

// --- Helpers ---

function loadPrivateKey() {
  return fs.readFileSync(STUDENT_PRIVATE_KEY_PATH, 'utf8');
}

function decryptSeed(encryptedSeedB64) {
  const encryptedBuffer = Buffer.from(encryptedSeedB64, 'base64');
  const privateKeyPem = loadPrivateKey();

  const decrypted = crypto.privateDecrypt(
    {
      key: privateKeyPem,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    encryptedBuffer
  );

  const hexSeed = decrypted.toString('utf8').trim();

  if (!/^[0-9a-f]{64}$/.test(hexSeed)) {
    throw new Error('Invalid seed format');
  }

  return hexSeed;
}

function saveSeed(hexSeed) {
  fs.mkdirSync(DATA_DIR, { recursive: true });
  fs.writeFileSync(SEED_FILE, hexSeed.trim(), { mode: 0o600 });
}

function loadSeed() {
  if (!fs.existsSync(SEED_FILE)) {
    return null;
  }
  return fs.readFileSync(SEED_FILE, 'utf8').trim();
}

function hexToBase32(hexSeed) {
  const bytes = Buffer.from(hexSeed, 'hex');
  const b32 = base32.encode(bytes).replace(/=+$/, '');
  return b32;
}

function generateTotpCode(hexSeed) {
  const secret = hexToBase32(hexSeed);
  return authenticator.generate(secret);
}

function verifyTotpCode(hexSeed, code, window = 1) {
  const secret = hexToBase32(hexSeed);
  const delta = authenticator.checkDelta(code, secret, { window });
  return delta !== null;
}

function getRemainingValiditySeconds() {
  const period = 30;
  const now = Math.floor(Date.now() / 1000);
  return period - (now % period);
}

// --- Routes ---

// POST /decrypt-seed
app.post('/decrypt-seed', (req, res) => {
  const { encrypted_seed } = req.body || {};
  if (!encrypted_seed) {
    return res.status(500).json({ error: 'Decryption failed' });
  }
  try {
    const hexSeed = decryptSeed(encrypted_seed);
    saveSeed(hexSeed);
    return res.json({ status: 'ok' });
  } catch (err) {
    console.error('decrypt-seed error:', err && err.stack ? err.stack : err.message || err);
    return res.status(500).json({ error: 'Decryption failed' });
  }
});
// GET /generate-2fa
app.get('/generate-2fa', (req, res) => {
  try {
    const hexSeed = loadSeed();
    if (!hexSeed) {
      return res.status(500).json({ error: 'Seed not decrypted yet' });
    }
    const code = generateTotpCode(hexSeed);
    const valid_for = getRemainingValiditySeconds();
    return res.json({ code, valid_for });
  } catch (err) {
    console.error('generate-2fa error:', err.message);
    return res.status(500).json({ error: 'Internal server error' });
  }
});

// POST /verify-2fa
app.post('/verify-2fa', (req, res) => {
  const { code } = req.body || {};

  if (!code) {
    return res.status(400).json({ error: 'Missing code' });
  }

  try {
    const hexSeed = loadSeed();
    if (!hexSeed) {
      return res.status(500).json({ error: 'Seed not decrypted yet' });
    }
    const valid = verifyTotpCode(hexSeed, code, 1); // ±1 period
    return res.json({ valid });
  } catch (err) {
    console.error('verify-2fa error:', err.message);
    return res.status(500).json({ error: 'Internal server error' });
  }
});

// Root test route (optional)
app.get('/', (req, res) => {
  res.json({ status: 'running', message: 'PKI-Based-2FA-Microservice' });
});

// --- Start server ---
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server listening on port ${PORT}`);
});