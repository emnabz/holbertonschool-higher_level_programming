#!/usr/bin/node

exports.converter = function (base) {
  function conv (num) {
    return num.toString(base);
  }
  return conv;
};
