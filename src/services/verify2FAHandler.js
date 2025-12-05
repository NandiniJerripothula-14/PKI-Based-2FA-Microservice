// src/services/verify2FAHandler.js
const { loadSeed } = require('./seedService');
const { verifyTotpCode } = require('../crypto/totp');

async function verify2FAHandler(req, res) {
  const { code } = req.body || {};

  if (!code) {
    return res.status(400).json({ error: 'Missing code' });
  }

  try {
    const hexSeed = await loadSeed();
    if (!hexSeed) {
      return res.status(500).json({ error: 'Seed not decrypted yet' });
    }

    const valid = verifyTotpCode(hexSeed, code, 1); // ±1 period
    return res.json({ valid });
  } catch (err) {
    console.error('verify-2fa endpoint error:', err.message);
    return res.status(500).json({ error: 'Internal server error' });
  }
}

module.exports = { verify2FAHandler };
