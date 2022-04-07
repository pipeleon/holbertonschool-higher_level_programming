#!/usr/bin/node
const process = require('process');

const nameFileA = process.argv[2];
const nameFileB = process.argv[3];
const nameFileC = process.argv[4];
let content;

const fs = require('fs');

content = fs.readFileSync(nameFileA, 'utf8');
content = content + '\n';
content = content + fs.readFileSync(nameFileB, 'utf8');

fs.writeFile(nameFileC, content, function (err) {
  if (err) throw err;
});
