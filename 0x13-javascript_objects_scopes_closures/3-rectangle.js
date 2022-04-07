#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      let row = 'X';
      for (let i = 1; i < this.width; i++) {
        row = row + 'X';
      }
      for (let j = 0; j < this.height; j++) {
        console.log(row);
      }
    }
  }
};
