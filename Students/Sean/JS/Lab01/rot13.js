const readline = require('readline-sync');

const from = 'abcdefghijklmnopqrstuvwxyz'
const to = 'nopqrstuvwxyzabcdefghijklm'
let roted = ''


function rot13(string){
    for (let i=0; i < string.length; i++){
        const index = from.indexOf(string[i]);
        roted += to[index]
    }
    return roted
}

try{
    let before = readline.question('enter string to convert: ');
   console.log(rot13(before))
}

catch(err){
    console.log("Enter a valid selection.")
}