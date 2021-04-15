const readline = require('readline-sync');
const alphabet = "abcdefghijklmnopqrstuvwxyz"
const keepSpecial = " 1234567890!@#$%^&*()_+=-,./;\\:'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
let alphabetArray = Array.from(alphabet);

let userString = readline.question("Please enter a string to be encoded: ");
let userRotationChoice = parseInt(readline.question("Please enter desired rotation: "));
let tempString = Array.from(userString);
let charLocationInAlphabet = 0;


for (i = 0; i < userString.length; i++){
    if (userString[i] == keepSpecial.){
        charLocationInAlphabet = alphabetArray.indexOf(userString[i])
        console.log("location 1 " + charLocationInAlphabet);
    
    
        tempString[i] = alphabetArray[(charLocationInAlphabet + userRotationChoice)%26] ;
        console.log("location 3 " + charLocationInAlphabet);
    }


        
        

}
console.log(tempString.join(""));
