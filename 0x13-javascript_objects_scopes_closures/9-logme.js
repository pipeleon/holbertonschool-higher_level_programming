#!/usr/bin/node
let count = 0;

exports.logMe = function (item) {
  const number = count + ':';
  console.log(number, item);
  count++;
};
