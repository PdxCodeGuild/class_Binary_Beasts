let start = document.getElementById('start');
let pause = document.getElementById('stop');
let lapBtn = document.getElementById('lapBtn');
let reset = document.getElementById('reset');
let stopwatch = document.getElementById('stopwatch');
let watchMin = document.getElementById('min');
let watchSec = document.getElementById('sec');
let watchMil = document.getElementById('mil');
let lapMin = document.getElementById('lapMin');
let lapSec = document.getElementById('lapSec');
let lapMil = document.getElementById('lapMil');

let mil = 0;
let sec = 0;
let min = 0;
let go;

function count() {
	mil += 1;
	if (mil > 59) {
		mil = 0;
		sec += 1;
		if (sec > 59) {
			sec = 0;
			min += 1;
		}
	}

	watchMin.innerHTML = `0${min}:`;
	if (min > 9) {
		watchMin.innerHTML = `${min}:`;
	}

	watchSec.innerHTML = `0${sec}:`;
	if (sec > 9) {
		watchSec.innerHTML = `${sec}:`;
	}

	watchMil.innerHTML = `0${mil}`;
	if (mil > 9) {
		watchMil.innerHTML = `${mil}`;
	}

	timer();
}

function timer() {
	go = setTimeout(count, 1);
}

window.setInterval(function () {
	let clock = new Date();
	document.getElementById('clock').innerHTML = clock;
}, 1000);

start.onclick = timer;

pause.onclick = function () {
	clearTimeout(go);
};

reset.onclick = function () {
	clearTimeout(go);
	mil = 0;
	sec = 0;
	min = 0;
	watchMin.innerHTML = '00:';
	watchSec.innerHTML = '00:';
	watchMil.innerHTML = '00';
	lapMin.innerHTML = '00:';
	lapSec.innerHTML = '00:';
	lapMil.innerHTML = '00';
};

lapBtn.onclick = function () {
	lapMin.innerHTML = watchMin.innerHTML;
	lapSec.innerHTML = watchSec.innerHTML;
	lapMil.innerHTML = watchMil.innerHTML;
};
