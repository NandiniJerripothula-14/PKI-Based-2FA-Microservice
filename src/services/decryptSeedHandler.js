// src/services/decryptSeedHandler.js
const { decryptSeed } = require('../crypto/rsa');
const { saveSeed } = require('./seedService');

async function decryptSeedHandler(req, res) {
  const { encrypted_seed } = req.body || {};

  if (!encrypted_seed) {
    // Spec: treat as failure, but they only specify 500 with "Decryption failed"
    return res.status(500).json({ error: 'Decryption failed' });
  }

  try {
    const hexSeed = decryptSeed(encrypted_seed);
    await saveSeed(hexSeed);
    return res.json({ status: 'ok' });
  } catch (err) {
    console.error('decrypt-seed endpoint error:', err.message);
    return res.status(500).json({ error: 'Decryption failed' });
  }
}

module.exports = { decryptSeedHandler };
