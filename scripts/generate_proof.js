const fs = require('fs');
const crypto = require('crypto');
const { execSync } = require('child_process');

try {
  // 1) get commit hash
  const commit = execSync('git rev-parse --verify HEAD').toString().trim();
  if (!/^[0-9a-f]{40}$/.test(commit)) throw new Error('Invalid commit hash: ' + commit);

  // 2) load keys (must exist in repo root)
  if (!fs.existsSync('student_private.pem')) throw new Error('Missing student_private.pem');
  if (!fs.existsSync('instructor_public.pem')) throw new Error('Missing instructor_public.pem');
  const priv = fs.readFileSync('student_private.pem', 'utf8');
  const instrPub = fs.readFileSync('instructor_public.pem', 'utf8');

  // 3) sign commit hash (ASCII) using RSA-PSS SHA-256, max salt
  const signer = crypto.createSign('sha256');
  signer.update(commit, 'utf8');
  signer.end();
  const signature = signer.sign({
    key: priv,
    padding: crypto.constants.RSA_PKCS1_PSS_PADDING,
    saltLength: crypto.constants.RSA_PSS_SALTLEN_MAX_SIGN
  });

  // 4) encrypt signature with instructor public key using OAEP-SHA256
  const encrypted = crypto.publicEncrypt({
    key: instrPub,
    padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
    oaepHash: 'sha256'
  }, signature);

  // 5) output
  console.log('Commit Hash:', commit);
  console.log('Encrypted Signature (base64):', encrypted.toString('base64'));
} catch (e) {
  console.error('ERROR:', e && (e.stack || e.message || e));
  process.exit(1);
}
