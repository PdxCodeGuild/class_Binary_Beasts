/*

all codes are written and created by John Robson Fri Mar 19, 2021

*/

export function runLab09() {
  renApp(
    [
      { el: "h1", text: "Lab 09 - ROT13 Cipher Tool" },
      { el: "label", text: "Enter rotation number 0 - 26" },
      { el: "input", cl: "rot", type: "number", min: 0, max: 26 },
      { el: "label", text: "Enter word to encrypt" },
      { el: "input", cl: "english", type: "text" },
      { el: "span", cl: "cipher" },
      { el: "div", cl: "cipher-box" },
    ],
    $("main")
  );

  $(".rot").addEventListener("input", () => {
    checkInput($(".rot"), 2);
  });
  $("input").onchange = generateLetters;

  $(".english").addEventListener("keydown", (e) => {
    if (e.key === "Backspace") {
      translate();
      return;
    }
    console.log(e.key);
    e.preventDefault();
    if ($(".rot").value === "") return;
    $(".english").value =
      $(".english").value + within(e.key.toLowerCase(), lowers);
    translate();
  });
}

const generateLetters = () => {
  checkValue($(".rot"), 0, 26);
  clear($(".cipher-box"));
  renApp(
    { el: "div", cl: "rot-eng rot-box", text: "English:" },
    $(".cipher-box")
  );
  lowers
    .split("")
    .forEach((l) =>
      renApp({ el: "div", cl: "rot-div rot-box", text: l }, $(".cipher-box"))
    );

  renApp(
    [{ el: "br" }, { el: "div", cl: "rot-ciph rot-box", text: "Cipher:" }],
    $(".cipher-box")
  );
  lowers.split("").forEach((l, i) =>
    renApp(
      {
        el: "div",
        cl: "rot-div rot-box",
        text: lowers[(i + parseInt($(".rot").value)) % 26],
      },
      $(".cipher-box")
    )
  );
};

const translate = () => {
  let buf = "";
  $(".english")
    .value.split("")
    .forEach((v) => {
      if (v === " ") buf += " ";
      else buf += lowers[(lowers.indexOf(v) + parseInt($(".rot").value)) % 26];
    });

  $(".cipher").innerText = buf;
};
