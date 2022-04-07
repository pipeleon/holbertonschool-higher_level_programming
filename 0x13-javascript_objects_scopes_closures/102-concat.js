#!/usr/bin/node
const process = require('process');

const nameFileA = process.argv[2];
const nameFileB = process.argv[3];
const nameFileC = process.argv[4];

const fs = require('fs')

fs.readFile(nameFileA, 'utf8' , (err, data1) => {
  if (err) {
    console.error(err)
    return
  }
  fs.writeFile(nameFileC, data1, function (err) {
    if (err) throw err;
  });
})


fs.readFile(nameFileB, 'utf8' , (err, data2) => {
  if (err) {
    console.error(err)
    return
  }
  fs.appendFile(nameFileC, '\n', function (err) {
    if (err) throw err;
  });
  fs.appendFile(nameFileC, data2, function (err) {
    if (err) throw err;
  });
})
