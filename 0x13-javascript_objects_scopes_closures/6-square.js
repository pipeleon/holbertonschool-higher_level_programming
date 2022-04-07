#!/usr/bin/node
class Rectangle {
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

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

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
