#!/usr/bin/node
const arlen = process.argv.length;

if (arlen === 2) {
	console.log('No argument');
} else if (arlen === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
	
