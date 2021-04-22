function returnRan(){
    return Math.floor((Math.random() * 256));
}

document.getElementById("change-color").addEventListener("click",function(){
    let rColor = document.getElementById("random-head");
    let returnString = `rgb(${returnRan()},${returnRan()},${returnRan()})`;
    rColor.style.color = returnString;
})



