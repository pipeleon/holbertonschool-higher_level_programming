#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c = 'X') {
    let row = c;
    for (let i = 1; i < this.width; i++) {
      row = row + c;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
};
