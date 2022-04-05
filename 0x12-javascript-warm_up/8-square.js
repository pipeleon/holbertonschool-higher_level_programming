#!/usr/bin/node
const process = require('process');
const number = parseInt(process.argv[2]);
let row = 'X';

if (number) {
  for (let i = 1; i < number; i++) {
    row = row + 'X';
  }
  for (let j = 0; j < number; j++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
