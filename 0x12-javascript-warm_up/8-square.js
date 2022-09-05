#!/usr/bin/node

/*
Write a script that prints a square

    The first argument is the size of the square
    If the first argument can’t be converted to an integer, print “Missing size”
    You must use the character X to print the square
    You must use console.log(...) to print all output
    You are not allowed to use var
    You must use a loop (while, for, etc.)

*/
const argv = process.argv;

if (argv.length < 3) {
  console.log('Missing size');
} else if (argv.length >= 3) {
  // Passed arguments start from index: 2
  const arg1 = argv[2];
  const size = parseInt(arg1);
  if (!isNaN(size)) {
    let row = '';
    for (let i = 0; i < size; i++) {
      row = row + 'X';
    }
    for (let j = 0; j < size; j++) {
      console.log(row);
    }
  } else {
    console.log('Missing size');
  }
}
