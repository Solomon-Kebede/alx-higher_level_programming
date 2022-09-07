#!/usr/bin/node

/*
Write a script that searches the second biggest integer in the list of arguments.

    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0
    You must use console.log(...) to print all output
    You are not allowed to use var

*/
const argv = process.argv;
// Passed arguments start from index: 2
if (argv.length <= 3) {
  console.log(0);
} else if (argv.length > 3) {
  // const args = argv.slice(2);
  // https://www.freecodecamp.org/news/javascript-array-sort-tutorial-how-to-use-js-sort-methods-with-code-examples/
  // The sort method, fortunately, can sort negative, zero, and positive values in the correct order
  console.log(argv.slice(2).sort(function (a, b) { return a - b; }).reverse()[1]);
  // console.log(argv.slice(2).sort().reverse()[1]);
}
