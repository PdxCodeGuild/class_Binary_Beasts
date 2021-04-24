const links = [
"https://www.google.com","https://www.wikipedia.com","https://www.yahoo.com"
]

function countdown(){
    let timer = 5;
    let count = setInterval(function(){
        if(timer<=0){
            clearInterval(count);
            document.getElementById("launch").innerHTML = "Bye!";
            window.location.assign(links[Math.round(Math.random() * (links.length - 1))]);
        }
        else {
            document.getElementById("launch").innerHTML = timer + " seconds until launch.";
        }
        timer -= 1;
}, 1)};

document.getElementById("launch").onclick = function(){countdown()};