const text_field = document.getElementById("weahter_input");
const key = apikey()
$("#btn").on('click', function(){
    console.log(text_field.value)
    fetch(`http://api.openweathermap.org/data/2.5/weather?q=${text_field.value}&appid=${key}`)
    // console.log(key)
    .then((response)=>{
    return response.json()
    })
    .then((data)=>{
        // console.log(data.weather[0].description)
        const weather = data.weather[0].description
        console.log(weather)
        const weatherDiv = document.getElementById("div1");
        div1.innerHTML = `<p>The Weather in ${text_field.value} is: ${weather}</p>`;
        if(weather == 'clear sky'){
            $('body').css({"background-color":"LightYellow"})
            var clearskyImg = document.createElement('img');
            clearskyImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/clearsky.png";
            document.getElementById('div1').appendChild(clearskyImg);
        }else if(weather == 'broken clouds'){
            $('body').css({"background-color":"DarkGray"})
            var brokencloudsImg = document.createElement('img');
            brokencloudsImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/broeknclouds.png";
            document.getElementById('div1').appendChild(brokencloudsImg);
        }else if(weather == 'scattered clouds'){
            $('body').css({"background-color":"Gray"})
            var scatteredcloudsImg = document.createElement('img');
            scatteredcloudsImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/scatteredclouds.png";
            document.getElementById('div1').appendChild( scatteredcloudsImg);
        }else if(weather == 'overcast clouds'){
            $('body').css({"background-color":"Gray"})
            var overcastcloudsImg = document.createElement('img');
            overcastcloudsImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/overcastclouds.png";
            document.getElementById('div1').appendChild(overcastcloudsImg);
        }else if(weather == 'few clouds'){
            $('body').css({"background-color":"LightGray"})
            var fewcloudsImg = document.createElement('img');
            fewcloudsImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/fewclouds.png";
            document.getElementById('div1').appendChild(fewcloudsImg);
        }else if(weather == 'shower rain'){
            $('body').css({"background-color":"Blue"})
            var showerrainImg = document.createElement('img');
            showerrainImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/showerrain.png";
            document.getElementById('div1').appendChild(showerrainImg);
        }else if(weather == 'rain'){
        $('body').css({"background-color":"DarkBlue"})
            var rainImg = document.createElement('img');
            rainImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/rain.png";
            document.getElementById('div1').appendChild(rainImg);
        }else if(weather == 'thunderstorm'){
            $('body').css({"background-color":"DarkBlue"})
            var thunderstormImg = document.createElement('img');
            thunderstormImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/thunderstorm.png";
            document.getElementById('div1').appendChild(thunderstormImg);
        }else if(weather == 'snow'){
            $('body').css({"background-color":"Gainsboro"})
            var snowImg = document.createElement('img');
            snowImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/snow.png";
            document.getElementById('div1').appendChild(snowImg);
        }else if(weather == 'mist'){
        $('body').css({"background-color":"LightBlue"})
            var mistImg = document.createElement('img');
            mistImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/mist.png";
            document.getElementById('div1').appendChild(mistImg);
        }else if(weather == 'light rain'){
            $('body').css({"background-color":"LightBlue"})
            var lightrainImg = document.createElement('img');
            lightrainImg.src = "/Users/dakotalowery/Desktop/PDX_Code_Guild/pdx_code/class_Binary_Beasts/Students/Dakota/JavaScript/LabWeatherAPI/weathericons/lightrain.png";
            document.getElementById('div1').appendChild(lightrainImg);
        }
    })
    .catch((error)=>{
        console.log(error)
    });
})