api_key = key();





function applyBackground(){
    bodyBackground = document.getElementById("color_change");
    bodyBackground.style.transition = "background-color 3s ease";
    bodyBackground.style.backgroundColor = "#00FFFF";
}

async function getWeather(){
    zip = document.getElementById("entered-zip").value;
    request = (`https://api.openweathermap.org/data/2.5/weather?zip=${zip}&appid=${api_key}`);
    console.log(`here is a request string: ${request}`);
    
    weather = await fetch(`https://api.openweathermap.org/data/2.5/weather?zip=${zip}&appid=${api_key}`);

    // weather = await fetch(`https://api.openweathermap.org/data/2.5/weather?zip=93454&appid=9f34511811a1858839fef8426d4ff511`);

    weather = await weather.json()
    console.log(weather['weather'][0]['main']);
    applyBackground();
}


