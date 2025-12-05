// src/services/seedService.js
const fs = require('fs');
const path = require('path');

const DATA_DIR = process.env.DATA_DIR || '/data';
const SEED_FILE = path.join(DATA_DIR, 'seed.txt');

function saveSeed(hexSeed) {
  return new Promise((resolve, reject) => {
    fs.mkdir(DATA_DIR, { recursive: true }, (err) => {
      if (err) return reject(err);
      fs.writeFile(SEED_FILE, hexSeed.trim(), { mode: 0o600 }, (err2) => {
        if (err2) return reject(err2);
        resolve();
      });
    });
  });
}

function loadSeed() {
  return new Promise((resolve, reject) => {
    fs.readFile(SEED_FILE, 'utf-8', (err, data) => {
      if (err) {
        if (err.code === 'ENOENT') return resolve(null); // missing seed
        return reject(err);
      }
      resolve(data.trim());
    });
  });
}

module.exports = { saveSeed, loadSeed, SEED_FILE };
