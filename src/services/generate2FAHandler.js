// src/services/generate2FAHandler.js
const { loadSeed } = require('./seedService');
const { generateTotpCode, getRemainingValiditySeconds } = require('../crypto/totp');

async function generate2FAHandler(req, res) {
  try {
    const hexSeed = await loadSeed();
    if (!hexSeed) {
      return res.status(500).json({ error: 'Seed not decrypted yet' });
    }

    const code = generateTotpCode(hexSeed);
    const valid_for = getRemainingValiditySeconds();

    return res.json({ code, valid_for });
  } catch (err) {
    console.error('generate-2fa endpoint error:', err.message);
    return res.status(500).json({ error: 'Internal server error' });
  }
}

module.exports = { generate2FAHandler };
