const fname = document.getElementById("fname"),
  form = document.querySelector("form");
(lname = document.getElementById("lname")),
  (email = document.getElementById("email")),
  (fError = document.getElementById("ferror")),
  (lError = document.getElementById("lerror")),
  (eError = document.getElementById("eerror")),
  (submit = document.querySelector("button")),
  (aRe = /[A-Z]/gi),
  (eRe = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/);

form.addEventListener("submit", (event) => {
  event.preventDefault();
  if (aRe.test(fname.value) && aRe.test(lname.value) && eRe.test(email.value))
    console.log("nice");
  else console.log("failed");
});

function post(url = "", data = {}) {
  const response = fetch(url, {
    method: "POST",
    redirect: "follow",
    body: JSON.stringify(data),
  });
  return response.json();
}
