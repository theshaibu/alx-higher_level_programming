#!/usr/bin/node

const { dict } = require('./101-data.js');
const newDict = {};

for (const key in dict) {
    if (Object.prototype.hasOwnProperty.call(dict, key)) {
        if (newDict[dict[key]] === undefined) {
            newDict[dict[key]] = [key];
        } else {
            newDict[dict[key]].push(key);
        }
    }
}

console.log(newDict);

