const fName_input = document.querySelector("#fName");
const fName_info = document.querySelector("#fName_info");
const lName_input = document.querySelector("#lName");
const lName_info = document.querySelector("#lName_info");
const email_input = document.querySelector("#email");
const email_info = document.querySelector("#email_info");
const submit_info = document.getElementById("submit");
const form_control = document.querySelector("#control");


fName_input.addEventListener("input", function () {
  const patternFname = /[a-z]\w+/g;
  if (!patternFname.test(this.value)) {
    this.style.outline = "1px solid red";
    fName_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    fName_info.style.display = "none";
  }
});

lName_input.addEventListener("input", function () {
  const patternLname = /[a-z]\w+/g;
  if (!patternLname.test(this.value)) {
    this.style.outline = "1px solid red";
    lName_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    lName_info.style.display = "none";
  }
});

email_input.addEventListener("input", function () {
  const pattern = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+.[com]{2,6}$/i;
  if (!pattern.test(this.value)) {
    this.style.outline = "1px solid red";
    email_info.style.display = "inline";
  } else {
    this.style.outline = "1px solid black";
    email_info.style.display = "none";
  }
});

fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((json) => console.log(json));

form_control.addEventListener("submit", function (event) {
    event.preventDefault()
    post_data()
    form_control.reset()
  
});
function post_data () {
fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  body: JSON.stringify({
    firstName: fName_input.value,
    LastName: lName_input.value,
    Email: email_input.value
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8",
  },
})
  .then((response) => response.json())
  .then((json) => console.log(json));
}