const readline = require('readline-sync');
const conv_dict = {
    "ft" : 0.3048,
    "mi" : 1609.34,
    "m"  : 1,
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254,
};

let distance = parseInt(readline.question('What is the distance?: '));
let starting_units = readline.question("What are the starting units?: ");
let units_to_convert_to = readline.question("What are the units to convert to?: ");


conv_distance = distance * conv_dict[starting_units];

conv_distance = conv_distance / conv_dict[units_to_convert_to];

conv_distance = conv_distance.toFixed(8);
conv_distance_split = conv_distance.split('.');


console.log(`${distance} ${starting_units} is ${Number(conv_distance)} ${units_to_convert_to}`);
    



