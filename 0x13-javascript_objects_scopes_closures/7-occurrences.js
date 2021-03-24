#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i;
  let j = 0;
  for (i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      j++;
    }
  }
  return j;
};
