/*
Theo R. Cocco
Monday April 12, 2021
Unit Converter Lab
*/

const readline = require("readline-sync");

//Version 1(Feet to meters)

/*
let ft = parseInt(readline.question('What distance in ft do you want converted? '))

console.log(`${ft}ft is ~${(ft *= .3048).toFixed(2)}m`)
*/

//Version 2(More units to meters)

/*
var units = {
  ft: 0.3048,
  mi: 1609.34,
  m: 1,
  km: 1000,
};

const unit = readline.question(
  "What unit do you want to want to convert to meters? "
);

if (unit in units) {
  let dist = parseInt(
    readline.question("What distance do you want to convert? ")
  );
  console.log(`${dist}${unit} is ${(dist *= units[unit]).toFixed(2)}m`);
} else {
  console.log(
    `${unit} is not a recognized unit, try again with "ft", "mi", "m", "km"`
  );
}
*/

//Version 3(Adding Yards and Inches)

/*
var units = {
  ft: 0.3048,
  mi: 1609.34,
  m: 1,
  km: 1000,
  yd: 0.9144,
  in: 0.0254,
};

const unit = readline.question(
  "What unit do you want to want to convert to meters? "
);

if (unit in units) {
  let dist = parseInt(
    readline.question("What distance do you want to convert? ")
  );
  console.log(`${dist}${unit} is ${(dist *= units[unit]).toFixed(2)}m`);
} else {
  console.log(
    `${unit} is not a recognized unit, try again with "ft", "mi", "m", "km", "yd", or "in"`
  );
}
*/

//Version 4(Convert to any unit)

var units = {
  ft: 0.3048,
  mi: 1609.34,
  m: 1,
  km: 1000,
  yd: 0.9144,
  in: 0.0254,
};

const from_unit = readline.question(
  "What unit do you want to want to convert? "
);

if (from_unit in units) {
  let to_unit = readline.question(
    "What unit do you want to want to convert to? "
  );
  if (to_unit in units) {
    let dist = parseInt(
      readline.question("What distance do you want to convert? ")
    );
    console.log(`${dist}${to_unit} is ${((dist *= units[from_unit]) / (units[to_unit])).toFixed(2)}m`);
  }
} else {
  console.log(
    `${unit} is not a recognized unit, try again with "ft", "mi", "m", "km", "yd", or "in"`
  );
}
