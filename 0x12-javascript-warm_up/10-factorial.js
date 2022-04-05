#!/usr/bin/node
const process = require('process');
const number = parseInt(process.argv[2]);

function factorial (a) {
  if (a) {
    if (a > 0) {
      return a * factorial(a - 1);
    } else {
      return 1;
    }
  } else {
    return 1;
  }
}

console.log(factorial(number));
