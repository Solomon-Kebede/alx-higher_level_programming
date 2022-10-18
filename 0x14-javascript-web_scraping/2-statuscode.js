#!/usr/bin/node

/*
Write a script that display the status code of a `GET` request.
  -The first argument is the URL to request (`GET`)
  -The status code must be printed like this: `code: <status code>`
  -You must use the module `request`
*/

// Include request module
const request = require('request');

// The first passed argument: url
const url = process.argv.slice(2)[0];

request(url, (error, response, body) => {
  if (error) {
    // Error handler
    return console.log(error);
  }
  // Printing status code
  console.log(`code: ${response.statusCode}`);
});
