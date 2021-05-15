const key = '1L1OFDGVRTTPDO3K';

let ticker1 = document.getElementById('TSLA');

let pastWeek = [160, 145, 180, 140, 185];

function getData() {
	fetch(
		`https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&outputsize=compact&apikey=${key}`
	)
		.then((response) => response.json())
		.then(function (data) {
			ticker1.innerHTML = data['Meta Data']['2. Symbol'];
			pastWeek.push(
				data['Time Series (Daily)']['2021-05-05']['5. adjusted close'],
				data['Time Series (Daily)']['2021-05-04']['5. adjusted close'],
				data['Time Series (Daily)']['2021-05-03']['5. adjusted close'],
				data['Time Series (Daily)']['2021-04-30']['5. adjusted close'],
				data['Time Series (Daily)']['2021-04-29']['5. adjusted close'],
			);
		});
}

getData();

console.log(pastWeek);

let myChart = document.getElementById('myChart').getContext('2d');

let stockChart = new Chart(myChart, {
  type:'bar',
  data:{
    labels:['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    datasets:[{
      label:'Closing price',
      data:[pastWeek[0], pastWeek[1], pastWeek[2], pastWeek[3], pastWeek[4]],
      backgroundColor:'blue',
      borderWidth:1,
      borderColor:'#777',
      hoverBorderWidth:3,
      hoverBorderColor:'#000'
    }]
  },
  options:{}

})