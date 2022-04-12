#!/usr/bin/node
const process = require('process');

const nameFileA = process.argv[2];

const fs = require('fs');

fs.readFile(nameFileA, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data1);
});
