#!/usr/bin/node

/*
Write a script that prints the number of movies where the character "Wedge Antilles" is present.
  -The first argument is the API URL of the [Star wars API](https://swapi-api.hbtn.io/): `https://swapi-api.hbtn.io/api/films/`
  -Wedge Antilles is character ID `18` - your script **must** use this ID for filtering the result of the API
  -You must use the module `request`
*/

// Include request module
const request = require('request');

// The first passed argument: url
const apiUrl = process.argv.slice(2)[0];
let count = 0;

request(apiUrl, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  // Parse json body
  const jsonData = JSON.parse(body);

  for (let i = 0; i < jsonData.results.length; i++) {
    const charactersList = jsonData.results[i].characters;
    for (let j = 0; j < charactersList.length; j++) {
      if (charactersList[j].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
