#!/usr/bin/node

/*
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

    Your script must import dict from the file 101-data.js
    In the new dictionary:
        A key is a number of occurrences
        A value is the list of user ids
    Print the new dictionary at the end

*/
// TODO: "Unknown" Correction Required!
const dict = require('./101-data').dict;
// console.log(dict);

const newKeys = new Set(Object.values(dict));
const newValues = Object.keys(dict);
const newDict = {};

for (const value of newKeys) {
  newDict[value] = [];
  // console.log(value);
  for (let i = 0; i < newValues.length; i++) {
    if (value === dict[newValues[i]]) {
      newDict[value].push(newValues[i]);
    }
  }
}
console.log(newDict);
