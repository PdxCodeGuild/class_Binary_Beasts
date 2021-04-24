api_key = key();


condition_dict = {
    "Clouds" : "CadetBlue",
    "Rain": "Azure",
    "Drizzle" : "Cyan",
    "Thunderstorm" : "DarkGrey",
    "Snow" : "GhostWhite",
    "Mist" : "Teal",
    "Smoke" : "Silver",
    "Haze" : "PapayaWhip",
    "Dust" : "OldLace",
    "Fog" : "LightSteelBlue",
    "Sand" : "LightSalmon",
    "Dust" : "Khaki",
    "Ash" : "Lavender",
    "Squall" : "Ivory",
    "Tornado": "FireBrick",
    "Clear" : "HoneyDew",

};

icon_dict = {
    "Clouds" : "fas fa-cloud",
    "Rain": "Azure",
    "Drizzle" : "Cyan",
    "Thunderstorm" : "fas fa-cloud-showers-heavy",
    "Snow" : "far fa-snowflake",
    "Mist" : "fas fa-cloud-showers-heavy",
    "Smoke" : "fas fa-sun",
    "Haze" : "fas fa-sun",
    "Dust" : "fas fa-sun",
    "Fog" : "LightSteelBlue",
    "Sand" : "fas fa-sun",
    "Dust" : "fas fa-sun",
    "Ash" : "fas fa-sun",
    "Squall" : "fas fa-sun",
    "Tornado": "fas fa-wind",
    "Clear" : "fas fa-sun",

};


function applyBackground(weather){
    weather = weather;
    bodyBackground = document.getElementById("color_change");
    bodyBackground.style.transition = "background-color 3s ease";
    bodyBackground.style.backgroundColor = condition_dict[weather['weather'][0]['main']];
}

async function getWeather(){
    zip = document.getElementById("entered-zip").value;
    
    weather = await fetch(`https://api.openweathermap.org/data/2.5/weather?zip=${zip}&appid=${api_key}&units=imperial`);


    weather = await weather.json()
    applyBackground(weather);

    ul = document.getElementById("current-weather");
    li = document.createElement("li");
    li.appendChild(document.createTextNode(`Main: ${weather['weather'][0]['main']}`));
    ul.appendChild(li);
    li = document.createElement("li");
    li.appendChild(document.createTextNode(`Description: ${weather['weather'][0]['description']}`));
    ul.appendChild(li);
    li = document.createElement("li");
    li.appendChild(document.createTextNode(`City: ${weather['name']}`));
    ul.appendChild(li);
    li = document.createElement("li");
    li.appendChild(document.createTextNode(`Temp: ${weather['main']['temp']}`));
    ul.appendChild(li);
    li = document.createElement("li");
    li.appendChild(document.createTextNode(`Feels Like: ${weather['main']['feels_like']}`));
    ul.appendChild(li);
    li = document.createElement("li");
    const icon = document.createElement("i");
    icon.setAttribute("class", `${icon_dict[weather['weather'][0]['main']]}`);
    li.appendChild(icon);
    ul.appendChild(li);
    


}


