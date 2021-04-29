const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const rot13Alphabet = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm";
const text_field = document.getElementById("user_input");
const output = document.getElementById("output");
const trigger = document.getElementById("button");
let encoded = '';
let encodedOut = '';
trigger.addEventListener("click", function () {
    output.innerText = text_field.value;
    encodedOut = output.innerText
    for (let i=0; i<encodedOut.length; i++) {
        const index = alphabet.indexOf(encodedOut[i]);
        encoded += rot13Alphabet[index];
    }
    rot13Word = document.getElementById("encoded")
    rot13Word.innerText = encoded
})
