// src/crypto/totp.js
const { authenticator } = require('otplib');
const base32 = require('hi-base32');

// Configure otplib (SHA-1, 30s, 6 digits are defaults, but we set them clearly)
authenticator.options = {
  step: 30,
  digits: 6,
  algorithm: 'SHA1',
};

// Convert hex seed (64-char) to base32
function hexToBase32(hexSeed) {
  const bytes = Buffer.from(hexSeed, 'hex');
  // hi-base32 encodes to uppercase base32
  const b32 = base32.encode(bytes).replace(/=+$/, ''); // remove padding
  return b32;
}

function generateTotpCode(hexSeed) {
  const secret = hexToBase32(hexSeed);
  const code = authenticator.generate(secret);
  return code; // "123456"
}

function verifyTotpCode(hexSeed, code, window = 1) {
  const secret = hexToBase32(hexSeed);
  // window = ±1 period (±30s)
  return authenticator.checkDelta(code, secret, { window }) !== null;
}

// Remaining validity seconds in current 30s window
function getRemainingValiditySeconds() {
  const period = 30;
  const now = Math.floor(Date.now() / 1000);
  const remaining = period - (now % period);
  return remaining;
}

module.exports = {
  generateTotpCode,
  verifyTotpCode,
  getRemainingValiditySeconds,
};
