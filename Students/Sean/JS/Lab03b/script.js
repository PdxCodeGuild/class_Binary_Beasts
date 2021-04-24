document.getElementById("randomize").onclick = function(){
    c1 = ~~(Math.random() * 255)
    c2 = ~~(Math.random() * 255)
    c3 = ~~(Math.random() * 255)
    document.getElementById("randomize").style = `background-color: rgb(${c1}, ${c2}, ${c3})`
}