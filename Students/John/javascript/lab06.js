/*

all codes are written and created by John Robson Fri Mar 19, 2021

*/

export function runLab06() {
  renApp(
    [
      { el: "h1", text: "Lab 06 - Random Password" },
      { el: "label", text: "How many lowercase letters?" },
      { el: "input", cl: "pw-input lower", type: "number", min: 0, max: 5 },
      { el: "label", text: "How many uppercase letters?" },
      { el: "input", cl: "pw-input upper", type: "number", min: 0, max: 5 },
      { el: "label", text: "How many special characters?" },
      { el: "input", cl: "pw-input special", type: "number", min: 0, max: 5 },
      { el: "label", text: "How many numbers?" },
      { el: "input", cl: "pw-input number", type: "number", min: 0, max: 5 },
      { el: "button", text: "Generate Password", cl: "password-btn" },
      { el: "aside", cl: "pw-aside" },
    ],
    $("main")
  );

  renApp({ el: "h2", text: "Passwords:" }, $(".pw-aside"));

  $(".password-btn").onclick = generatePassword;

  $$("input").forEach((i) =>
    i.addEventListener("input", () => {
      checkInput(i, 1);
      checkValue(i, 0, 5);
    })
  );
}

const generatePassword = () => {
  if (checkValid()) {
    getData();
  }
};

const checkValid = () => {
  return notNullV([$(".lower"), $(".upper"), $(".special"), $(".number")]);
};

const getData = () => {
  limit($$(".pw"), 5)
  let l = parseInt($(".lower").value),
    u = parseInt($(".upper").value),
    s = parseInt($(".special").value),
    n = parseInt($(".number").value);

  l = randI(lowers, l);
  u = randI(uppers, u);
  s = randI(special, s);
  n = randI(numbers, n);

  let password = [...l, ...u, ...s, ...n];
  renApp(
    {
      el: "p",
      cl: "pw",
      text: shuffle(password).toString().split(",").join(""),
    },
    $(".pw-aside")
  );
};
