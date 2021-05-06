const Form = document.querySelector('form');

Form.addEventListener('submit', function (e) {
	e.preventDefault();
	validCheck();
});

// function validCheck() {
// 	let Fname = document.getElementById('Fname');
// 	let Lname = document.getElementById('Lname');
// 	let Email = document.getElementById('Email');

// 	document.getElementById('Fcheck').style.display = 'none';
// 	Fname.style.outline = 'none';

// 	document.getElementById('Lcheck').style.display = 'none';
// 	Lname.style.outline = 'none';

//   document.getElementById('Echeck').style.display = 'none';
//   Email.style.outline = 'none';

// 	const regex = /^[a-zA-Z]+$/g;

// 	const regexEmail = /([a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+.[a-zA-z0-9]+)/g;

// 	if (!regex.test(Fname.value)) {
// 		document.getElementById('Fcheck').style.display = 'inline';
// 		Fname.style.outline = '1px solid red';
// 	} else if (regex.test(Fname.value)) {
// 		document.getElementById('Fcheck').style.display = 'none';
// 		Fname.style.outline = 'none';
// 	}


// 	if (!regex.test(Lname.value)) {
// 		document.getElementById('Lcheck').style.display = 'inline';
// 		Lname.style.outline = '1px solid red';
// 	} else if (regex.test(Lname.value)) {
// 		document.getElementById('Lcheck').style.display = 'none';
// 		Lname.style.outline = 'none';
// 	}


// 	if (!regexEmail.test(Email.value)) {
// 		document.getElementById('Echeck').style.display = 'inline';
// 		Email.style.outline = '1px solid red';
// 	} else if (regexEmail.test(Email.value)) {
// 		document.getElementById('Echeck').style.display = 'none';
// 		Email.style.outline = 'none';
// 	}

//   Why does this not return "true true true"?
//   console.log(
// 	  regex.test(Fname.value),
//     regex.test(Lname.value),
// 		regexEmail.test(Email.value),
// 	)
// 	if (
// 		regex.test(Fname.value) &&
// 		regex.test(Lname.value) &&
// 		regexEmail.test(Email.value)
// 	) {
//     Fname.style.outline = '3px solid green';
  
//     Lname.style.outline = '3px solid green';
  
//     Email.style.outline = '3px solid green';
// 	}
// }


function validCheck() {
	let Fname = document.getElementById('Fname');
	let Lname = document.getElementById('Lname');
	let Email = document.getElementById('Email');

	document.getElementById('Fcheck').style.display = 'none';
	Fname.style.outline = 'none';
  firstTest = false

	document.getElementById('Lcheck').style.display = 'none';
	Lname.style.outline = 'none';
  lastTest = false

  document.getElementById('Echeck').style.display = 'none';
  Email.style.outline = 'none';
  emailTest = false

	const regexF = /^[a-zA-Z]+$/g;

  const regexL = /^[a-zA-Z]+$/g;

	const regexEmail = /([a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+.[a-zA-z0-9]+)/g;

	if (!regexF.test(Fname.value)) {
		document.getElementById('Fcheck').style.display = 'inline';
		Fname.style.outline = '1px solid red';
	} else {
		document.getElementById('Fcheck').style.display = 'none';
		Fname.style.outline = 'none';
    firstTest = true
	}


	if (!regexL.test(Lname.value)) {
		document.getElementById('Lcheck').style.display = 'inline';
		Lname.style.outline = '1px solid red';
	} else {
		document.getElementById('Lcheck').style.display = 'none';
		Lname.style.outline = 'none';
    lastTest = true
	}


	if (!regexEmail.test(Email.value)) {
		document.getElementById('Echeck').style.display = 'inline';
		Email.style.outline = '1px solid red';
	} else {
		document.getElementById('Echeck').style.display = 'none';
		Email.style.outline = 'none';
    emailTest = true
	}

  if (firstTest == true){
    if (lastTest == true){
      if (emailTest == true){
        data = {
        "userId": Fname.value,
        "id": 1,
        "title": Lname.value,
        "body": Email.value,
        }

        fetch('https://jsonplaceholder.typicode.com/posts', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then(response => response.json())
        .then(data => {
          console.log('Success', data);
        })
        .catch((error) => {
          console.error('Error', error);
        })
      }
    }
  }
}