#!/usr/bin/node

/*
Write a script that computes and prints a factorial

    The first argument is integer (argument can be cast as integer) used for computing the factorial
    Factorial of NaN is 1
    You must do it recursively
    You must use a function
    You must use console.log(...) to print all output
    You are not allowed to use var

*/
const argv = process.argv;
// Passed arguments start from index: 2
const arg1 = argv[2];

function factorial (x) {
  if (x === 1) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}

if (isNaN(arg1)) {
  console.log(1);
} else {
  console.log(factorial(arg1));
}
