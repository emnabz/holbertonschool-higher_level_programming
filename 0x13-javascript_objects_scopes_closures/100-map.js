#!/usr/bin/node

const list = require('./100-data').list;
let array = 0;
const List1 = list.map(x => x * array++);
console.log(list);
console.log(List1);
