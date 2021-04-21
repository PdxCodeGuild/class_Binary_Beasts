//Unit Converter Version 1
// const readline = require('readline-sync');
// let userInput = parseInt(readline.question('what is the distance in feet?'));
// console.log(`you entered: ${userInput} ft`);
// var converted = (userInput * 0.3048);
// console.log(`${userInput} ft is ${converted} m`);

//Unit Converter Version 2
// const readline = require('readline-sync');
// let distance = parseInt(readline.question('what is the distance? '));
// let unit = readline.question('What is the units? ');
// let converted = ''
// if (unit === 'feet'){
//     converted = distance * 0.3048;
// } 
// else if (unit === 'miles'){
//     converted = distance * 1609.34;
// } 
// else if (unit === 'meters'){
//     converted = distance * 1;
// } 
// else if (unit === 'kilometers'){
//     converted = distance * 1000;
// } 
// console.log(`${distance} ${unit} is ${converted} m`);

//Unit Converter Version 3
// const readline = require('readline-sync');
// let distance = parseInt(readline.question('what is the distance? '));
// let unit = readline.question('What is the units? ');
// let converted = ''
// if (unit === 'feet'){
//     converted = distance * 0.3048;
// } 
// else if (unit === 'miles'){
//     converted = distance * 1609.34;
// } 
// else if (unit === 'meters'){
//     converted = distance * 1;
// } 
// else if (unit === 'kilometers'){
//     converted = distance * 1000;
// } 
// else if (unit === 'yards'){
//     converted = distance * 0.9144;
// } 
// else if (unit === 'inch'){
//     converted = distance * 0.0254;
// } 
// console.log(`${distance} ${unit} is ${converted} m`);

//Unit Converter Version 4
const readline = require('readline-sync');
let distance = parseInt(readline.question('what is the distance? '));
let inUnit = readline.question('What are the input units? ');
let outUnit = readline.question('What are the output units? ');
let converted = ''
let outConverted = ''
if (inUnit === 'feet'){
    converted = distance * 0.3048;
    if (outUnit == 'miles'){
        outConverted = converted / 1609.34;
    }
    else if (inUnit === 'meters'){
        converted = distance * 1;
        outConverted = converted / 1;
    } 
    else if (inUnit === 'kilometers'){
        converted = distance * 1000;
        outConverted = converted / 1000;
} 
else if (inUnit === 'miles'){
    converted = distance * 1609.34;
    if (outUnit == 'feet'){
        outConverted = converted / 0.3048;
    }
    else if (inUnit === 'meters'){
        converted = distance * 1;
        outConverted = converted / 1;
    } 
    else if (inUnit === 'kilometers'){
        converted = distance * 1000;
        outConverted = converted / 1000;
} 
else if (inUnit === 'meters'){
    converted = distance * 1;
    outConverted = converted / 1;
    if (outUnit == 'feet'){
        outConverted = converted / 0.3048;
    }
    else if (outUnit == 'miles'){
        outConverted = converted / 1609.34;
    }
    else if (inUnit === 'kilometers'){
        converted = distance * 1000;
        outConverted = converted / 1000;
    } 
} 
else if (inUnit === 'kilometers'){
    converted = distance * 1000;
    if (outUnit == 'feet'){
        outConverted = converted / 0.3048;
    }
    else if (outUnit == 'miles'){
        outConverted = converted / 1609.34;
    }
    else if (inUnit === 'meters'){
        converted = distance * 1;
        outConverted = converted / 1;
    } 
} 
console.log(`${distance} ${inUnit} is ${outConverted} ${outUnit}`);