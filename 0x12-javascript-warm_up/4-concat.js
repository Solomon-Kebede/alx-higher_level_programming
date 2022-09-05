#!/usr/bin/node

/*
Write a script that prints two arguments passed to it, in the following format: “ is ”

    You must use console.log(...) to print all output
    You are not allowed to use var

*/
const argv = process.argv;
// Passed arguments start from index: 2
const arg1 = argv[2];
const arg2 = argv[3];

console.log(`${arg1} is ${arg2}`);
