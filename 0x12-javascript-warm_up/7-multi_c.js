#!/usr/bin/node

/*
Write a script that prints x times “C is fun”

    Where x is the first argument of the script
    If the first argument can’t be converted to an integer, print “Missing number of occurrences”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You can use only two console.log
    You must use a loop (while, for, etc.)

*/
const argv = process.argv;

function error () {
  console.log('Missing number of occurrences');
}

if (argv.length < 3) {
  error();
} else if (argv.length >= 3) {
  // Passed arguments start from index: 2
  const arg1 = argv[2];
  const x = parseInt(arg1);
  if (!isNaN(x)) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  } else {
    error();
  }
}
