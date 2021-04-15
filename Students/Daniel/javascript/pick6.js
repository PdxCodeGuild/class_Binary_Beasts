const priceSheet = {
    "ticketCost" : 2,
    "0" : 0,
    "1" : 4,
    "2"  : 7,
    "3" : 100,
    "4" : 50000,
    "5" : 1000000,
    "6" : 25000000,
};
let winningTicket = pick6();
let generatedTickets = runTimes(100000);
let accountBalance = 0;
let roi = 0;
let runningTally = 0;

function pick6(){
    let pick6_array = [];
    for (i = 0; i <= 5; i++) {
        pick6_array.push(Math.floor((Math.random() * 99) + 1));
    }
    return pick6_array;
}

function runTimes(amount){
    let tempArr = []
    for( x = 1; x <=amount; x++){  
        tempArr.push(pick6());
    }
    return tempArr;
}

function num_matches(winning, ticket){
    accountBalance = 0;
    roi = 0;
    for(i = 0; i<= ticket.length-1; i++){
        runningTally = 0;
        for(x=0; x<= 5; x++){
            if (winning[x] == ticket[i][x]){
                runningTally = runningTally + 1;
            }
            
        }
        accountBalance = accountBalance - priceSheet["ticketCost"] + priceSheet[runningTally];
    }
    expenses = generatedTickets.length * priceSheet["ticketCost"]
    expenses = -Math.abs(expenses);
    earnings = accountBalance;
    roi = (earnings - expenses)/ expenses;
}


num_matches(winningTicket,generatedTickets);
console.log(accountBalance);


