#!/usr/bin/node
const process = require('process');
const numberA = parseInt(process.argv[2]);
const numberB = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(numberA, numberB));
