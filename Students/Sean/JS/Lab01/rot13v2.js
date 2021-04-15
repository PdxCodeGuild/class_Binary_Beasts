function rotAny(msg, rot){
    const alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if(rot<0){rot=rot*-1}
    if(rot>26){rot=rot%26}

    console.log(rot)
    roted = msg.replace(/[a-z]/gi, letter => alphabet[alphabet.indexOf(letter) + rot])
    return roted
}

console.log(rotAny('Hello, hello',520001))