#!/usr/bin/node
const len = parseInt(process.argv[2]);

if (isNaN(len) || len === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < len; i++) {
    console.log('C is fun');
  }
}
