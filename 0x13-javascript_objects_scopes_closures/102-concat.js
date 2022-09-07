#!/usr/bin/node

/*
Write a script that concats 2 files.

    The first argument is the file path of the first source file
    The second argument is the file path of the second source file
    The third argument is the file path of the destination

*/

const argv = process.argv;
const args = argv.slice(2);

const fs = require('fs');

const content1 = fs.readFileSync(args[0], 'utf8');
const content2 = fs.readFileSync(args[1], 'utf8');

function write (path, content) {
  fs.writeFile(path, content, err => {
    if (err) {
      console.error(err);
    }
    // file written successfully
  });
}

const content = content1 + content2;
write(args[2], content);
