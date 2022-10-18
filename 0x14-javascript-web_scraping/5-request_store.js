#!/usr/bin/node

/*
Write a script that gets the contents of a webpage and stores it in a file.
  -The first argument is the URL to request
  -The second argument the file path to store the body response
  -The file must be UTF-8 encoded
  -You must use the module `request`
*/

// Include fs module and request modules
const fs = require('fs');
const request = require('request');

// The first passed argument: url
// The second passed argument: filePath
const url = process.argv.slice(2)[0];
const filePath = process.argv.slice(2)[1];

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  // Retrieve body and write to file
  fs.writeFile(filePath, body, 'utf-8', function (err) {
    if (err) {
      return console.log(err);
    }
  });
});
