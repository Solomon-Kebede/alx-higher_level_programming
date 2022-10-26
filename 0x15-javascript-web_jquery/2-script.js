/*
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:
  -You can’t use `document.querySelector` to select the HTML tag
  -You must use the JQuery API
*/

const header = $('header');
const redHeader = $('div#red_header');

redHeader.click(function () {
  header.css('color', '#FF0000');
});
