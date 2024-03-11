#!/usr/bin/node
// a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const firstArg = process.argv[2];
const parsedArg = parseInt(firstArg);

if (!isNaN(parsedArg)) {
    console.log(`My number: ${parsedArg}`);
} else {
    console.log("Not a number");
}

