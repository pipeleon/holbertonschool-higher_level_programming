#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c = 'X') {
    let row = c;
    for (let i = 1; i < this.size; i++) {
      row = row + c;
    }
    for (let j = 0; j < this.size; j++) {
      console.log(row);
    }
  }
};
