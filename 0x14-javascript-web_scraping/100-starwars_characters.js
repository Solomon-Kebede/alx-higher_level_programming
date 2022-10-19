#!/usr/bin/node

/*
Write a script that prints all characters of a Star Wars movie:
  -The first argument is the Movie ID - example: `3` = "Return of the Jedi"
  -Display one character name by line
  -You must use the [Star wars API](https://swapi-api.hbtn.io)
  -You must use the module `request`
*/

// Include request module
const request = require('request');

// The first passed argument: movieID
const movieID = process.argv.slice(2)[0];

// url to be requested
const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieID}`;

// Get info on a specific character
function getCharacter (peopleUrl) {
  const options = {
    url: peopleUrl,
    headers: {
      'User-Agent': 'request',
      Accept: 'application/json'
    }
  };
  function callback (error, response, body) {
    if (!error && response.statusCode === 200) {
      const info = JSON.parse(body);
      console.log(info.name);
    }
  }
  return request(options, callback);
}

request(movieUrl, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  // Parse json body
  const characterUrls = JSON.parse(body).characters;
  // List characters in the order they came
  for (let i = 0; i < characterUrls.length; i++) {
    getCharacter(characterUrls[i]);
  }
});
