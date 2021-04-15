const readline = require('readline-sync');

let before = readline.question('enter distance to convert: ');
const unit = readline.question('convert from: 0=ft, 1=mi, 2=m, 3=km, 4=yard, 5=inches ');
const after = readline.question('convert to: 0=ft, 1=mi, 2=m, 3=km, 4=yard, 5=inches ');

accepts = [0,1,2,3,4,5]

d = {
    "ist":[.3048,1609.34,1,1000,.9144,.0254]
}

try{
    before = parseFloat(before)
    if (unit in accepts && after in accepts){
        result = before * d.ist[unit] * d.ist[after]
        console.log(result)   
    }
}
catch(err){
    console.log("Enter a valid selection.")
}