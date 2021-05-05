let mymap = L.map('mapid').setView([51.505, -0.09], 13);

myKey = key();

L.tileLayer(
	`https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=` +
		myKey,
	{
		attribution:
			'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		maxZoom: 18,
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1,
		accessToken: 'your.mapbox.access.token',
	}
).addTo(mymap);

let popup = L.popup();

function onMapClick(e) {
	popup.setLatLng(e.latlng).setContent(e.latlng.toString()).openOn(mymap);
}

mymap.on('click', onMapClick);

window.onload = axios
	.get('https://jsonplaceholder.typicode.com/users')
	.then((response) => {
		for (i = 0; i < response.data.length; i++) {
			let lat = response.data[i].address.geo.lat;
			let lng = response.data[i].address.geo.lng;
			let marker = L.marker([lat, lng]).addTo(mymap);

			let name = response.data[i].name;
			let street = response.data[i].address.street;
			let city = response.data[i].address.city;
			let suite = response.data[i].address.suite;
			let zipCode = response.data[i].address.zipcode;

			marker.bindPopup(
				`<b>${name}</b><p>${street}, ${suite}, ${city}, ${zipCode}`
			);
			document.getElementById(
				'info'
			).innerHTML += `<li>${name}, in ${city}.</li>`;
		}
	});
