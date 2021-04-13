const readline = require('readline-sync');
let userInput = parseInt(readline.question('What is the distance in feet?: '));
conv_distance = userInput * 0.3048
conv_distance = conv_distance.toFixed(4);
console.log(`${userInput} ft is ${conv_distance} m`);