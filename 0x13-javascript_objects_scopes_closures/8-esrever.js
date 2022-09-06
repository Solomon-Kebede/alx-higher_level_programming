#!/usr/bin/node

/*
Write a function that returns the reversed version of a list:

    Prototype: `exports.esrever = function (list)`
    You are not allow to use the built-in method `reverse`
*/

exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    reversed[j] = list[i];
  }
  return (reversed);
};
