#!/usr/bin/node

/*
Write a script that writes a string to a file.
  -The first argument is the file path
  -The second argument is the string to write
  -The content of the file must be written in `utf-8`
  -If an error occurred during while writing, print the error object

*/

// Include fs module
const fs = require('fs');

// The first passed argument: filePath
// The second argument: string to write
const filePath = process.argv.slice(2)[0];
const string = process.argv.slice(2)[1];

// Use fs.writeFile() method to write to file
fs.writeFile(filePath, string, 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
