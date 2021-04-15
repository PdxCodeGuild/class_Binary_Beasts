/*
Theo Cocco
Wednesday April 14th, 2021
Pick 6 Lab
*/

const winningNumbers = [];

var winnings = {
  0: 0,
  1: 4,
  2: 7,
  3: 100,
  4: 50000,
  5: 1000000,
  6: 25000000,
};

let i = 0;

while (i < 6) {
  winningNumbers.push(Math.round(Math.random() * 99));
  i++;
}

function pick6() {
  let x = 0;
  let ticket = [];
  while (x < 6) {
    ticket.push(Math.round(Math.random() * 99));
    x++;
  }
  return ticket;
}

function checkWinners() {
  let matches = 0;
  let y = pick6();
  y.forEach(function (item) {
    if (winningNumbers.includes(item)) matches += 1;
  });
  return matches;
}

function balance() {
  let b = -20000;
  for (let i = 0; i < 10000; i++) {
    b += winnings[checkWinners()];
  }
  return b;
}

function roi() {
    return 
}

// console.log(`You won $${balance()}`) Version 1

const total = balance();
console.log(` you won $${total}, your ROI was ${((total - 20000) / 20000).toFixed(2)}`)