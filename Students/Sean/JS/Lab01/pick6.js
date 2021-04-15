const array_length = 6
const lucky6 = []
let balance = 0
let expenses = 0

let getRandomNumber = function(min, max){
    let getRandom = Math.floor((Math.random() * max) + min)
    while (getRandom > max) {
        getRandom = Math.floor((Math.random() * max) + min)
    }
    return getRandom
}

for(let i = 0; i<array_length; i++){
    lucky6.push(getRandomNumber(1, 99))
}

function gamble(x){
    let pick6 = []
    let matches = 0

    for(let i = 0; i<x; i++){
        pick6 = []
        balance -= 2
        matches = 0
        expenses += 2
        for(let i = 0; i<array_length; i++){
            pick6.push(getRandomNumber(1, 99))
        }
        for(let i = 0; i<array_length; i++){
            if (lucky6[i] === pick6[i]){
                matches += 1
            }
        }
        if (matches === 6){balance += 25000000}
        else if (matches === 5){balance += 1000000}
        else if (matches === 4){balance += 50000}
        else if (matches === 3){balance += 100}
        else if (matches === 2){balance += 7}
        else if (matches === 1){balance += 4}
        else if (matches === 0){balance += 0}
    }
}

gamble(100)

Rate = balance / expenses
console.log(`Your ROI was ${Rate}`)
console.log(`Your ending balance was ${balance}`)