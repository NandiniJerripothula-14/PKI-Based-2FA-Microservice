// src/routes.js
const express = require('express');
const router = express.Router();

const { decryptSeedHandler } = require('./services/decryptSeedHandler');
const { generate2FAHandler } = require('./services/generate2FAHandler');
const { verify2FAHandler } = require('./services/verify2FAHandler');

// POST /decrypt-seed
router.post('/decrypt-seed', decryptSeedHandler);

// GET /generate-2fa
router.get('/generate-2fa', generate2FAHandler);

// POST /verify-2fa
router.post('/verify-2fa', verify2FAHandler);

module.exports = router;
