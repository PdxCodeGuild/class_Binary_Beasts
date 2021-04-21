function randomWeb () {
    let webArray = ['https://www.instagram.com', 'https://dakotalowery42.github.io', 'https://github.com/PdxCodeGuild/class_Binary_Beasts', 'https://scuffletownsuppliers.com'];
    for (let i = 0; i < 4; i++){
        randomWebsites = Math.round(Math.random() * 3);
    }
    return webArray[randomWebsites]
    }
const randomWebpage = document.getElementById('randomWebpage')
randomWebpage.addEventListener("click", function () {
    var seconds = document.getElementById("countdown").textContent;
    var countdown = setInterval(function() {
    seconds--;
    document.getElementById("countdown").textContent = seconds;
    if (seconds <= 0) {
        window.open(randomWeb(), "_blank"); clearInterval(countdown)
    }
    else if (seconds < 0) {
        clearInterval(countdown);
    }
}, 500);
})
