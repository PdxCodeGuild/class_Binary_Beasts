const my_key = key();

function getWeather(city) {
	fetch(
		'https://api.openweathermap.org/data/2.5/weather?q=' +
			city +
			'&appid=' +
			my_key
	)
		.then(function (response) {
			return response.json();
		})
		.then(function (data) {
			postWeather(data);
		})
		.catch(function (err) {
			console.error(err);
		});
}

function postWeather(data) {
	document.getElementById('desc').innerHTML = data.weather[0].description;
	document.getElementById('temp').innerHTML = Math.round(
		(parseFloat(data.main.temp) - 273.15) * 1.8 + 32
	);
	document.getElementById('loc').innerHTML = data.name;

	if ((parseFloat(data.main.temp) - 273.15) * 1.8 + 32 > 69) {
		document.getElementById('temp').innerHTML +=
			'<p class="fas fa-temperature-high"></p>';
	} else if ((parseFloat(data.main.temp) - 273.15) * 1.8 + 32 <= 69) {
		document.getElementById('temp').innerHTML +=
			'<p class="fas fa-temperature-low"></p>';
	}

	console.log(data.weather[0].description);

	if (data.weather[0].description.includes('rain')) {
		(document.getElementById('main').style =
			'background: rgb(4,2,22);background: linear-gradient(168deg, rgba(4,2,22,1) 0%, rgba(8,57,121,1) 50%, rgba(30,32,43,1) 100%);'),
			(document.getElementById('box').innerHTML =
				'<i class="fas fa-cloud-showers-heavy"></i>');
	} else if (data.weather[0].description.includes('cloud')) {
		(document.getElementById('main').style =
			'background: rgb(54,169,224);background: linear-gradient(45deg, rgba(54,169,224,1) 0%, rgba(128,130,131,1) 64%);'),
			(document.getElementById('box').innerHTML =
				'<i class="fas fa-cloud"></i>');
	} else if (data.weather[0].description.includes('clear')) {
		(document.getElementById('main').style =
			'background: rgb(230,113,0);background: radial-gradient(circle, rgba(230,113,0,1) 0%, rgba(247,255,0,1) 100%);'),
			(document.getElementById('box').innerHTML = '<i class="far fa-sun"></i>');
	}
}
const btn = document.getElementById('search');
btn.addEventListener('click', function () {
	let input = document.getElementById('city').value;
	getWeather(input);
	document.getElementById('city').value = '';
});
