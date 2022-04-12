#!/usr/bin/node
const process = require('process');

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

const fs = require('fs');

fs.writeFileSync(filePath, stringToWrite, function (err) {
  if (err) {
    console.error(err);
  }
});
