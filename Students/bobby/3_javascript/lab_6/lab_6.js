var mymap = L.map("mapid").setView([51.505, -0.09], 13);
const myKey = key();

L.tileLayer(
  "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: "mapbox/streets-v11",
    tileSize: 512,
    zoomOffset: -1,
    accessToken: `${myKey}`,
  }
).addTo(mymap);

var circle = L.circle([51.508, -0.11], {
  color: "red",
  fillColor: "#f03",
  fillOpacity: 0.5,
  radius: 500,
}).addTo(mymap);

var polygon = L.polygon([
  [51.509, -0.08],
  [51.503, -0.06],
  [51.51, -0.047],
]).addTo(mymap);

circle.bindPopup("I am a circle.");
polygon.bindPopup("I am a polygon.");

var popup = L.popup()
  .setLatLng([51.5, -0.09])
  .setContent("I am a standalone popup.")
  .openOn(mymap);
var popup = L.popup();

function onMapClick(e) {
  popup
    .setLatLng(e.latlng)
    .setContent("You clicked the map at " + e.latlng.toString())
    .openOn(mymap);
}

mymap.on("click", onMapClick);

fetch("https://jsonplaceholder.typicode.com/users")
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    function createLi(name, username, email) {
      const $li =
        "<li>" +
        `Name: ${name}, Username: ${username}, Email: ${email}` +
        "</li>";
      $("#info").append($li);
      console.log($li);
    }
    for (let key in data) {
      var marker = L.marker(data[key].address.geo, data[key].address.geo).addTo(
        mymap
      );
      marker
        .bindPopup(
          `Lat${data[key].address.geo.lat}Lon${data[key].address.geo.lng}
      , ${data[key].name}, ${data[key].address.street}, ${data[key].address.suite}
      , ${data[key].address.city}, ${data[key].address.zipcode}`
        )
        .openPopup();
      createLi(data[key].name, data[key].username, data[key].email);
    }
  })
  .catch(function (error) {
    console.log(error);
  });
var div = $("h1");
div.animate({height: '300px', opacity: '0.4'}, "slow");
div.animate({width: '300px', opacity: '0.8'}, "slow");
div.animate({height: '100px', opacity: '0.4'}, "slow");
div.animate({width: '100px', opacity: '0.8'}, "slow");
div.animate({width: '500px', opacity: '0.8'}, "slow");
