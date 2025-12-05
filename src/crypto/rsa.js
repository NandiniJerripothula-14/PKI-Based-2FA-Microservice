// src/crypto/rsa.js
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const STUDENT_PRIVATE_KEY_PATH = process.env.STUDENT_PRIVATE_KEY_PATH || path.join(__dirname, '../../student_private.pem');
const INSTRUCTOR_PUBLIC_KEY_PATH = process.env.INSTRUCTOR_PUBLIC_KEY_PATH || path.join(__dirname, '../../instructor_public.pem');

const studentPrivateKeyPem = fs.readFileSync(STUDENT_PRIVATE_KEY_PATH, 'utf-8');
const instructorPublicKeyPem = fs.readFileSync(INSTRUCTOR_PUBLIC_KEY_PATH, 'utf-8');

function decryptSeed(encryptedSeedB64) {
  try {
    const encryptedBuffer = Buffer.from(encryptedSeedB64, 'base64');

    const decrypted = crypto.privateDecrypt(
      {
        key: studentPrivateKeyPem,
        padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
        oaepHash: 'sha256',
      },
      encryptedBuffer
    );

    const hexSeed = decrypted.toString('utf-8').trim();

    if (!/^[0-9a-f]{64}$/.test(hexSeed)) {
      throw new Error('Invalid seed format');
    }

    return hexSeed;
  } catch (err) {
    console.error('decryptSeed error:', err.message);
    throw err;
  }
}

// RSA-PSS-SHA256 sign
function signMessage(message) {
  const sign = crypto.createSign('sha256');
  sign.update(message, 'utf-8');
  sign.end();
  const signature = sign.sign({
    key: studentPrivateKeyPem,
    padding: crypto.constants.RSA_PKCS1_PSS_PADDING,
    saltLength: crypto.constants.RSA_PSS_SALTLEN_MAX_SIGN,
  });
  return signature; // Buffer
}

// Encrypt data with instructor public key using OAEP-SHA256
function encryptWithPublicKey(dataBuffer) {
  const encrypted = crypto.publicEncrypt(
    {
      key: instructorPublicKeyPem,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    dataBuffer
  );
  return encrypted; // Buffer
}

module.exports = {
  decryptSeed,
  signMessage,
  encryptWithPublicKey,
};
