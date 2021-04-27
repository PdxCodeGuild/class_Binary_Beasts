const myKey = key();

$("#button-addon1").on("click", function () {
  var img = $("img");
  img.animate({ height: "300px", opacity: "0.4" }, "slow");
  img.animate({ width: "300px", opacity: "0.8" }, "slow");
  img.animate({ height: "100px", opacity: "0.4" }, "slow");
  img.animate({ width: "100px", opacity: "0.8" }, "slow");
  const city = $("#cityInput").val();
  getData(city);
});

function getData(city) {
  fetch(
    `http://api.weatherstack.com/current?access_key=${myKey}&query=${city}&units=f`
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      document.getElementById("city").innerText = `City: ${data.location.name}`;
      document.getElementById(
        "time"
      ).innerText = `Date/Time: ${data.location.localtime}`;
      document.getElementById(
        "temp"
      ).innerText = `Temperature: ${data.current.temperature}`;
      document.getElementById("icon").src = data.current.weather_icons;
      document.getElementById(
        "description"
      ).innerText = `Description: ${data.current.weather_descriptions}`;
      let description = document.getElementById("description");
      let main = document.querySelector("main");
      if (description.innerText.toUpperCase() == `DESCRIPTION: PARTLY CLOUDY`) {
        main.style.backgroundColor = `grey`;
      } else if (
        description.innerText.toUpperCase() == `DESCRIPTION: CLEAR/SUNNY`
      ) {
        main.style.backgroundColor = `orange`;
      } else if (
        description.innerText.toUpperCase() == `DESCRIPTION: OVERCAST`
      ) {
        main.style.backgroundColor = `#EEE`;
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}

