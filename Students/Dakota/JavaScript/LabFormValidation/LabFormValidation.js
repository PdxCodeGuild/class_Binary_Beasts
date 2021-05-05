const Username = document.getElementById("Username");
const Usernametrigger = document.getElementById("submit");
Username.addEventListener("input", function () {
  console.log(Username.value);
  const Usernamepattern = /^[A-z]{6,}$/;
  if (!Usernamepattern.test(this.value)) {
    this.style.outline = "1px solid red";
    username_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    username_info.style.display = "none";
  }
});
const Password = document.getElementById("Password");
const Passwordtrigger = document.getElementById("submit");
Password.addEventListener("input", function () {
  console.log(Password.value);
  const Passwordpattern = /^[A-z]{6,}$/;
  if (!Passwordpattern.test(this.value)) {
    this.style.outline = "1px solid red";
    password_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    password_info.style.display = "none";
  }
});
const firstName = document.getElementById("firstName");
const firstNametrigger = document.getElementById("submit");
firstName.addEventListener("input", function () {
  console.log(firstName.value);
  const firstNamepattern = /^[A-z]{1,}$/;
  if (!firstNamepattern.test(this.value)) {
    this.style.outline = "1px solid red";
    firstName_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    firstName_info.style.display = "none";
  }
});
const lastName = document.getElementById("lastName");
const lastNametrigger = document.getElementById("submit");
lastName.addEventListener("input", function () {
  console.log(lastName.value);
  const lastNamepattern = /^[A-z]{1,}$/;
  if (!lastNamepattern.test(this.value)) {
    this.style.outline = "1px solid red";
    lastName_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    lastName_info.style.display = "none";
  }
});
const email = document.getElementById("email");
const emailtrigger = document.getElementById("submit");
email.addEventListener("input", function () {
  console.log(email.value);
  const emailpattern = /.[a-zA-Z0-9]{1,}@[^.]{1,}/;
  if (!emailpattern.test(this.value)) {
    this.style.outline = "1px solid red";
    email_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    email_info.style.display = "none";
  }
});
const Phone = document.getElementById("Phone");
const Phonetrigger = document.getElementById("submit");
Phone.addEventListener("input", function () {
  console.log(Phone.value);
  const Phonepattern = /^\d{3}-\d{3}-\d{4}$/;
  if (!Phonepattern.test(this.value)) {
    this.style.outline = "1px solid red";
    Phone_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    Phone_info.style.display = "none";
  }
});
const DOB = document.getElementById("DOB");
const DOBtrigger = document.getElementById("submit");
DOB.addEventListener("input", function () {
  console.log(DOB.value);
  const DOBpattern = /(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d/;
  if (!DOBpattern.test(this.value)) {
    this.style.outline = "1px solid red";
    DOB_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    DOB_info.style.display = "none";
  }
});
const Social = document.getElementById("Social");
const Socialtrigger = document.getElementById("submit");
Social.addEventListener("input", function () {
  console.log(Social.value);
  const Socialpattern = /^\d{3}-\d{2}-\d{4}$/;
  if (!Socialpattern.test(this.value)) {
    this.style.outline = "1px solid red";
    Social_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    Social_info.style.display = "none";
  }
});

const submitTrigger = document.getElementById("submit");
submitTrigger.addEventListener("click", function (e) {
  e.preventDefault();
  fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    body: JSON.stringify({
      Username: Username.value,
      Password: Password.value,
      FirstName: firstName.value,
      LastName: lastName.value,
      email: email.value,
      Phone: Phone.value,
      DateOfBirth: DOB.value,
      Social: Social.value,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((json) => console.log(json));
});
