const readline = require('readline-sync');
const alphabet = "abcdefghijklmnopqrstuvwxyz"
let alphabetArray = Array.from(alphabet);

let userString = readline.question("Please enter a string to be encoded: ");

console.log(userString);
console.log(alphabetArray[25]);
let tempString = "";
for (i = 0; i < userString.length; i++){
    console.log(userString.indexOf(userString[i]));
    tempString = tempString + alphabetArray[alphabetArray.indexOf(userString[i]) + 13] ;
}
console.log(tempString);
