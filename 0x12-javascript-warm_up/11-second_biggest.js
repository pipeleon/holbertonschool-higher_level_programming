#!/usr/bin/node
const process = require('process');

if (process.argv[3]) {
  const list = [];
  for (let i = 2; process.argv[i]; i++) {
    list.push(parseInt(process.argv[i]));
  }
  list.sort(function (a, b) { return b - a; });
  console.log(list[1]);
} else {
  console.log(0);
}
