let myInput = document.getElementById('addItem');
let toDo = document.getElementById('toDoList');
let completed = document.getElementById('completed');
let allItems = document.getElementsByTagName('li');

function addToList() {
	let li = document.createElement('li');
	let input = document.getElementById('addItem').value;
	let text = document.createTextNode(input);
	li.appendChild(text);
	document.getElementById('toDoList').appendChild(li);
	document.getElementById('addItem').value = '';

	let x = document.createElement('button');

	x.addEventListener('click', function () {
		try {
			toDo.removeChild(li);
		} catch (err) {
			completed.removeChild(li);
		}
	});

	x.innerHTML = 'X';
	x.className = 'clear';
	li.appendChild(x);

	let check = document.createElement('button');
	check.addEventListener('click', function () {
		toDo.removeChild(li);
		li.removeChild(check);
		completed.appendChild(li);
	});
	check.innerHTML = '&#10003';
	check.className = 'check';
	li.appendChild(check);
}

function clearList() {
	let list = document.getElementsByTagName('ul');
	list[0].innerHTML = '';
	list[1].innerHTML = '';
	document.getElementById('addItem').value = '';
}
