#!/usr/bin/node

const squarePrev = require('./5-square');
module.exports = class square extends squarePrev {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let space1 = '';
      for (let i = 0; i < this.width; i++) {
        space1 += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(space1);
      }
    }
  }
};
