#!/usr/bin/env node
require('dotenv').config();
const fs = require('fs');
const path = require('path');
const { loadSeed } = require('../src/services/seedService');
const { generateTotpCode } = require('../src/crypto/totp');
(async () => {
  try {
    const hexSeed = await loadSeed();
    if (!hexSeed) {
      console.error('Seed not decrypted yet');
      process.exit(1);
    }

    const code = generateTotpCode(hexSeed);

    // UTC timestamp: YYYY-MM-DD HH:MM:SS
    const now = new Date();
    const year = now.getUTCFullYear();
    const month = String(now.getUTCMonth() + 1).padStart(2, '0');
    const day = String(now.getUTCDate()).padStart(2, '0');
    const hours = String(now.getUTCHours()).padStart(2, '0');
    const minutes = String(now.getUTCMinutes()).padStart(2, '0');
    const seconds = String(now.getUTCSeconds()).padStart(2, '0');

    const timestamp = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    console.log(`${timestamp} - 2FA Code: ${code}`);
  } catch (err) {
    console.error('Cron error:', err.message);
    process.exit(1);
  }
})();
