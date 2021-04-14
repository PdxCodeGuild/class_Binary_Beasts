const readline = require('readline-sync');
let pick6_array = [];

for (i = 0; i <= 6; i++) {
    pick6_array.push(Math.floor((Math.random() * 99) + 1))
}


console.log(pick6_array);
