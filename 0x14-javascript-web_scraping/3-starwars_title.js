#!/usr/bin/node

/*
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
    -The first argument is the movie ID
    -You must use the [Star wars API](https://swapi-api.hbtn.io/) with the endpoint `https://swapi-api.hbtn.io/api/films/:id`
    -You must use the module `request`
*/

// Include request module
const request = require('request');

// The first passed argument: movieID
const movieID = process.argv.slice(2)[0];

// url to be requested
const url = `https://swapi-api.hbtn.io/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  // Parse json body
  console.log(JSON.parse(body).title);
});
