#!/usr/bin/node
const len = parseInt(process.argv[2]);
if (isNaN(len) || len === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < len; i++) {
    let str = '';
    for (let j = 0; j < len; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
