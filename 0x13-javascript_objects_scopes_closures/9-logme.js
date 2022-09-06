#!/usr/bin/node

/*
Write a function that prints the number of arguments already printed and the new argument value. (see example below)

    Prototype: exports.logMe = function (item)
    Output format: <number arguments already printed>: <current argument value>
*/

const list = [];
let count;

exports.logMe = function (item) {
  count = list.push(item);
  console.log(`${count - 1}: ${item}`);
};
