#!/usr/bin/node

const variable = process.argv[2];
if (isNaN(variable) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + variable);
}
