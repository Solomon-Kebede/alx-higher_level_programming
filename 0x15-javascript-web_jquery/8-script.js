/*
Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`
  -All movie titles must be list in the HTML tag `UL#list_movies`
  -You can’t use `document.querySelector` to select the HTML tag
  -You must use the JQuery API
*/

const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = $('ul#list_movies');

const res = $.getJSON(apiUrl, function () {
  const results = res.responseJSON.results;
  for (let i = 0; i < results.length; i++) {
    listMovies.append(`<li>${results[i].title}</li>`);
  }
});
