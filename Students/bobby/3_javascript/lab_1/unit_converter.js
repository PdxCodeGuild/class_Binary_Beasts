const readline = require('readline-sync');
// let userInput = parseInt(readline.question('enter a number: '));
// console.log(`you entered: ${userInput}`);

// Version 1
let userInput = parseFloat(readline.question("Enter the number of feet you would like to convert to meters: "));

console.log(`${userInput} feet is equal to ${userInput * .3048} meters`)