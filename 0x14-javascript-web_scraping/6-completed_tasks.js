#!/usr/bin/node

/*
Write a script that computes the number of tasks completed by user id.
  -The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
  -Only print users with completed task
  -You must use the module `request`
*/

// Include request module
const request = require('request');

// The first passed argument: url
const apiUrl = process.argv.slice(2)[0];

request(apiUrl, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  // Parse json body
  const jsonData = JSON.parse(body);
  const store = {};
  let userId = '';

  for (let i = 0; i < jsonData.length; i++) {
    userId = jsonData[i].userId;
    if (jsonData[i].completed) {
      if (isNaN(store[userId])) {
        store[userId] = 1;
      } else if (!isNaN(store[userId])) {
        store[userId]++;
      }
    }
  }
  console.log(store);
});
