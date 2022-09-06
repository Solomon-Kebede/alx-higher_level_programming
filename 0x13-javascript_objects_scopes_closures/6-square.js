#!/usr/bin/node

/*
Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`:

    You must use the `class` notation for defining your class and `extends`
    Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
        If `c` is `undefined`, use the character `X`

*/

const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    let ch = 'X';
    let char = '';
    if (c !== undefined) {
      ch = c;
    }

    for (let i = 0; i < this.size; i++) {
      char = char + ch;
    }
    for (let i = 0; i < this.size; i++) {
      console.log(char);
    }
  }
}

module.exports = Square;
