const readline = require('readline-sync');
const conv_dict = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m"  : 1,
    "km" : 1000,
};

let userDistance = parseInt(readline.question('What is the distance in feet?: '));
let userUnits = readline.question("What are the current units?: ");


conv_distance = userDistance * conv_dict[userUnits];
conv_distance = conv_distance.toFixed(4);
console.log(`${userDistance} ${userUnits} is ${conv_distance} m`);


