const button = document.getElementById("button");
button.addEventListener("click", function () {
    const title = document.getElementById("title");
    var randomColor = Math.floor(Math.random()*16777215).toString(16);
    title.style.color = "" + randomColor;
});