function randomTicket(){
    let ticketArray = []
    let randomNumbers = 0
    for (let i = 0; i < 6; i++){
        randomNumbers = Math.round(Math.random() * 99);
        ticketArray.push(randomNumbers);
    }
    return ticketArray
}
function matches(myRandomTicket, winTicket){
    let matches = 0;
    for (let i = 0; i < 6; i++){
        if (winTicket[i] == myRandomTicket[i]){
            // console.log(matches)
        }
    }
    return matches
}
let chance = 0;
let balance = 0;
let expenses = 0;
let payoff = 0;
let myRandomTicket = []
let winTicket = []
while (chance < 100000){
    chance++;
    balance -= 2
    expenses += 2
    myRandomTicket = randomTicket()
    winTicket = randomTicket()
    for (let i = 0; i < winTicket.length; i++) {
        if (winTicket[i] == myRandomTicket[i]){
            winMatches = matches(myRandomTicket, winTicket)
            const numMatches = {
                1 : 4,
                2 : 7,
                3 : 100,
                4 : 50000,
                5 : 1000000,
                6 : 25000000
            }
        }
        else {
            loseMatches = matches(myRandomTicket, winTicket)
            winMatches = matches(myRandomTicket, winTicket)
        }
    }
        const numMatches = {
            1 : 4,
            2 : 7,
            3 : 100,
            4 : 50000,
            5 : 1000000,
            6 : 25000000
    }
        for (key in numMatches){
            if (winMatches === key){
                console.log(winMatches)
                balance += numMatches[key]
            }
        }    
}
netWinngings = (balance - expenses)
ROI = (netWinngings)/expenses
console.log(`Total earnings equal to ${netWinngings}`)
console.log(`ROI ${ROI}`)
