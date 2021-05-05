// 1 Display the Map
var mymap = L.map('mapid').setView([35.78, -78.64], 1);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(mymap);
var homepopup = L.popup()
    .setLatLng([35.78, -78.64])
    .setContent("Wait, they don't love you like I love you...")
    .openOn(mymap);
// 2 Get the data for the ten users from jsonplaceholder
fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then((data)=>{
// 3 From that data, extract the latitude and longitude associated with each user
    const u1 = data[0].address.geo
    const u2 = data[1].address.geo
    const u3 = data[2].address.geo
    const u4 = data[3].address.geo
    const u5 = data[4].address.geo
    const u6 = data[5].address.geo
    const u7 = data[6].address.geo
    const u8 = data[7].address.geo
    const u9 = data[8].address.geo
    const u10 = data[9].address.geo
// 4 Display a marker on the map marking their location using the extracted lat/lon values. Note: these locations will be in weird places, that's ok.
    var u1marker = L.circle([u1["lat"],u1["lng"]], {color: 'pink'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
    var u2marker = L.circle([u2["lat"],u2["lng"]], {color: 'black'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
    var u3marker = L.circle([u3["lat"],u3["lng"]], {color: 'pink'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
    var u4marker = L.circle([u4["lat"],u4["lng"]], {color: 'black'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
    var u5marker = L.circle([u5["lat"],u5["lng"]], {color: 'pink'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
    var u6marker = L.circle([u6["lat"],u6["lng"]], {color: 'black'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
    var u7marker = L.circle([u7["lat"],u7["lng"]], {color: 'pink'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
    var u8marker = L.circle([u8["lat"],u8["lng"]], {color: 'black'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
    var u9marker = L.circle([u9["lat"],u9["lng"]], {color: 'pink'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
    var u10marker = L.circle([u10["lat"],u10["lng"]], {color: 'black'}, {flillColor: '#f03'}, {fillOpacity: 0.5}, {radius: 500}).addTo(mymap);
   
// 5 Create a popup for the marker. When the marker is clicked, a popup should show (see the imgage below) containing information about the name and address of the user associated with that location.
    let u1popup = L.popup()
        .setLatLng([u1["lat"],u1["lng"]])
        u1marker.bindPopup(`<b>${data[0].name}</b><br>${data[0].address.street}<br>${data[0].address.suite}<br>${data[0].address.city}<br>${data[0].address.zipcode}`);
    let u2popup = L.popup()
        .setLatLng([u2["lat"],u2["lng"]])
        u2marker.bindPopup(`<b>${data[1].name}</b><br>${data[1].address.street}<br>${data[1].address.suite}<br>${data[1].address.city}<br>${data[1].address.zipcode}`);
    let u3popup = L.popup()
        .setLatLng([u3["lat"],u3["lng"]])
        u3marker.bindPopup(`<b>${data[2].name}</b><br>${data[2].address.street}<br>${data[2].address.suite}<br>${data[2].address.city}<br>${data[2].address.zipcode}`);
    let u4popup = L.popup()
        .setLatLng([u4["lat"],u4["lng"]])
        u4marker.bindPopup(`<b>${data[3].name}</b><br>${data[3].address.street}<br>${data[3].address.suite}<br>${data[3].address.city}<br>${data[3].address.zipcode}`);
    let u5popup = L.popup()
        .setLatLng([u5["lat"],u5["lng"]])
        u5marker.bindPopup(`<b>${data[4].name}</b><br>${data[4].address.street}<br>${data[4].address.suite}<br>${data[4].address.city}<br>${data[4].address.zipcode}`);
    let u6popup = L.popup()
        .setLatLng([u6["lat"],u6["lng"]])
        u6marker.bindPopup(`<b>${data[5].name}</b><br>${data[5].address.street}<br>${data[5].address.suite}<br>${data[5].address.city}<br>${data[5].address.zipcode}`);
    let u7popup = L.popup()
        .setLatLng([u7["lat"],u7["lng"]])
        u7marker.bindPopup(`<b>${data[6].name}</b><br>${data[6].address.street}<br>${data[6].address.suite}<br>${data[6].address.city}<br>${data[6].address.zipcode}`);
    let u8popup = L.popup()
        .setLatLng([u8["lat"],u8["lng"]])
        u8marker.bindPopup(`<b>${data[7].name}</b><br>${data[7].address.street}<br>${data[7].address.suite}<br>${data[7].address.city}<br>${data[7].address.zipcode}`);
    let u9popup = L.popup()
        .setLatLng([u9["lat"],u9["lng"]])
        u9marker.bindPopup(`<b>${data[8].name}</b><br>${data[8].address.street}<br>${data[8].address.suite}<br>${data[8].address.city}<br>${data[8].address.zipcode}`);
    let u10popup = L.popup()
        .setLatLng([u10["lat"],u10["lng"]])
        u10marker.bindPopup(`<b>${data[9].name}</b><br>${data[0].address.street}<br>${data[9].address.suite}<br>${data[9].address.city}<br>${data[9].address.zipcode}`);
})
fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then((data)=>{
      // 6 Display some other information for the users in a different part of the page, off the map. I chose to stuff everything below the map. I encourage (but am not requiring) you to be more creative.
        let users = document.querySelector("#users")
        users.innerHTML += `<b>Name: </b>${data[0].name}, <b>Username: </b>${data[0].username}, <b>Email: </b>${data[0].email}<br>`
        users.innerHTML += `<b>Name: </b>${data[1].name}, <b>Username: </b>${data[1].username}, <b>Email: </b>${data[1].email}<br>`
        users.innerHTML += `<b>Name: </b>${data[2].name}, <b>Username: </b>${data[2].username}, <b>Email: </b>${data[2].email}<br>`
        users.innerHTML += `<b>Name: </b>${data[3].name}, <b>Username: </b>${data[3].username}, <b>Email: </b>${data[3].email}<br>`
        users.innerHTML += `<b>Name: </b>${data[4].name}, <b>Username: </b>${data[4].username}, <b>Email: </b>${data[4].email}<br>`
        users.innerHTML += `<b>Name: </b>${data[5].name}, <b>Username: </b>${data[5].username}, <b>Email: </b>${data[5].email}<br>`
        users.innerHTML += `<b>Name: </b>${data[6].name}, <b>Username: </b>${data[6].username}, <b>Email: </b>${data[6].email}<br>`
        users.innerHTML += `<b>Name: </b>${data[7].name}, <b>Username: </b>${data[7].username}, <b>Email: </b>${data[7].email}<br>`
        users.innerHTML += `<b>Name: </b>${data[8].name}, <b>Username: </b>${data[8].username}, <b>Email: </b>${data[8].email}<br>`
        users.innerHTML += `<b>Name: </b>${data[9].name}, <b>Username: </b>${data[9].username}, <b>Email: </b>${data[9].email}<br>`
  })