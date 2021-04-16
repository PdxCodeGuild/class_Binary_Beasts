const readline = require('readline-sync');

// Version 1

// let userInput = parseFloat(readline.question("Enter the number of feet you would like to convert to meters: "));

// console.log(`${userInput} feet is equal to ${userInput * .3048} meters`)

//-----------------------------------------------------------------------------

// Version 2

// const conversion = {
//     ft : .3048,
//     mi : 1609.34,
//     m : 1,
//     km : 1000
// }

// let units = readline.question("Enter the units you would like to convert to meters (ft, mi, m, km): ");
// let distance = parseFloat(readline.question("Enter the distance you would like to convert to meters: "));

// console.log(`${distance} ${units} is equal to ${distance * (conversion[units])} meters`)  

//-------------------------------------------------------------------------------------

// Version 3

// const conversion = {
//     ft : .3048,
//     mi : 1609.34,
//     m : 1,
//     km : 1000,
//     yrd : .9144,
//     in : .0254
// }

// let units = readline.question("Enter the units you would like to convert to meters (ft, mi, m, km, yrd, in): ");
// let distance = parseFloat(readline.question("Enter the distance you would like to convert to meters: "));

// console.log(`${distance} ${units} is equal to ${distance * (conversion[units])} meters`)

//-----------------------------------------------------------------------------------------

// Version 4

// const conversion = {
//     ft : .3048,
//     mi : 1609.34,
//     m : 1,
//     km : 1000,
//     yrd : .9144,
//     in : .0254
// }

// let units_from = readline.question("Enter the units you would like to convert from (ft, mi, m, km, yrd, in): ");
// let units_to = readline.question("Enter the units you would like to convert to (ft, mi, m, km, yrd, in): ");
// let distance = parseFloat(readline.question("Enter the distance you would like to convert to meters: "));

// const result = (`${conversion[units_from] * distance / conversion[units_to]}`)

// console.log(`${distance} ${units_from} is equal to ${result} ${units_to}`)

//--------------------------------------------------------------------------------------------

// Pick 6, Versions 1 & 2


// function pick6() {
//     const nums = []
//     for (let i = 0; i < 6; i++) { // starting at 0, stopping at 6, advancig one each time
//         let ranNumbs = Math.floor((Math.random() * 100) + 1); // Picking random #'s from 1 to 99
//        nums.push(ranNumbs) // Pushes random #'s to array nums
//     }
//     return nums
// }

// const winNumbs = pick6() // This calls my pick6 function

// const earnings = 0

// function earnCalc(match, earnings) { // This function calculates my earnings
//     if (match === 0) {
//         earnings -= 2;
//     } else if (match === 1) {
//         earnings += 4;
//     } else if (match === 2) {
//         earnings += 7;
//     } else if (match === 3) {
//         earnings += 100;
//     } else if (match === 4) {
//         earnings += 50000;
//     } else if (match === 5) {
//         earnings += 1000000;
//     } else if (match === 6) {
//         earnings += 25000000;
//     } return earnings // this returns my earnings
// }
// earnCalc() // This calls my function earnCalc

// let count = 0 // this tracks my count
// let total = 0 // this tracks my total

// for (let i = 0; i < 200; i++) { // starting at 0, stopping at 100,000, advancig one each time
//     count += 1 // This adds my game count each time thrjough the loop
//     let match = 0; // This tracks my matches
//     let play = pick6(); // New variable play for variable pick6
//     console.log(`Player numbers= ${play}`) // This prints the palyer tickets
//     for (let i = 0; i < winNumbs.length; i++) { // starting at 0, stopping at the length of winNumbs, advancig one each time
//         if (winNumbs[i] === play[i]) { // conditional that compares each number at it's indicies
//             match += 1 // adds to the matches by one each time through the loop
//         }
//     }
//     total += earnCalc(match, earnings)
// }
// console.log(`count= ${count}`)
// const expenses = total - (count * 2)
// const roi = (total - expenses) / expenses

// console.log(`Winning numbers= ${winNumbs}`)

// console.log(`Earnings= ${total}`)
// console.log(`Expenses= ${expenses}`)
// console.log(`ROI= ${Math.round(roi * 100)}%`)

//--------------------------------------------------------------------------------------------

// Rot 13, Versions 1

// var engList = "abcdefghijklmnopqrstuvwxyz".split(""); // this is my array of lower case letters used in the cipher

// let userInput = readline.question("Enter the information you wish to Cipher. "); // input from user to cipher

// for (let i = 0; i < userInput.length; i++) { // starting at 0, stopping at length of the input, advancig one each time
//     const a = (engList.indexOf(userInput[i]) + 13) % 26 // variable a is english list at the index of the user input + 13
//                                                         // and by using the modulous character with the total length of the list
//                                                         // it takes me back to the beginning when +13 goes beyond 26
//     console.log(engList[a]) 
// }

//--------------------------------------------------------------------------------------------

// Rot 13, Versions 2 (THIS VERSION DOES NOT WORK YET)

// var engList = "abcdefghijklmnopqrstuvwxyz".split(""); // this is my array of lower case letters used in the cipher

// let userInput = readline.question("Enter the information you wish to Cipher. "); // input from user to cipher
// let userRot = parseInt(readline.question("Enter the amount of rotation. ")); // input from user for the rotation changed to integer

// for (let i = 0; i < userInput.length; i++) { // starting at 0, stopping at length of the input, advancig one each time
//     const a = (engList.indexOf(userInput[i]) + (userRot)) % 26  // variable a is english list at the index of the user input + rotation input
//                                                                 // and by using the modulous character with the total length of the list
//                                                                 // it takes me back to the beginning when +13 goes beyond 26
//     console.log(engList[a]) 
// }

