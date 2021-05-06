document.getElementById("submit").addEventListener("click", function (event) {
  event.preventDefault()
  const userInput = document.querySelectorAll(".input");

  const nameRegex = new RegExp('(^[A-Za-z]+$)');
  const emailRegex = new RegExp('([@])');
  fname = userInput[0].value;
  lname = userInput[1].value;
  email = userInput[2].value;
  if (!nameRegex.test(fname) || (!nameRegex.test(lname)) || (!emailRegex.test(email))) {
    document.getElementById("userForm").reset();
    console.log("Form reset");
  } else {
    axios.post('https://jsonplaceholder.typicode.com/posts', {
      firstName: fname,
      lastName: lname,
      email: email
    })
      .then((response) => {
        console.log(response);

      }, (error) => {
        console.log(error);
      });
  }




});