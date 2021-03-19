/*

all codes are written and created by John Robson Fri Mar 19, 2021

*/

export function runLab03() {
  renApp(
    [
      { el: "h1", text: "Lab 03 - Grading" },
      { el: "label", text: "Please enter a score 0 - 100" },
      { el: "input", cl: "score", type: "number", min: 0, max: 100 },
      { el: "h2", cl: "grade" },
      { el: "aside", cl: "history" },
    ],
    $("main")
  );

  renApp(
    [
      { el: "h2", text: "History" },
      { el: "div", cl: "hist-container" },
    ],
    $(".history")
  );

  $(".score").addEventListener("input", checkInput);
  $(".score").onchange = checkValue;
}

function checkInput() {
  const el = $(".score");
  if (!parseInt(el.value)) el.value = null;
  if (el.value.length > 3) el.value = el.value.substring(1);
}

function checkValue() {
  const el = $(".score");
  if (el.value < 0) el.value = 0;
  else if (el.value > 100) el.value = 100;
  else el.value = Math.round(el.value);

  if (el.value != null) updateGrade();
}

function updateGrade() {
  const el = $(".grade");
  el.innerText = "Grade: " + calcGrade();

  addToHistory();
}

function calcGrade() {
  const s = $(".score").value;

  const m = Math.max,
    f = Math.floor,
    g = "ABCDF",
    j = (a, b, c) => (a ? b : c);

  return (
    g[g.length + j(s == 100, -5, f(-m(10, s - 49) / 10))] +
    j(s == 100, "++", j(s < 60, "", j(s % 10 < 4, "-", j(s % 10 > 6, "+", ""))))
  );
}

function addToHistory() {
  $(".hist-container");
  $(".grade").innerText.split(": ")[1];

  let query = $(".score").value + ": " + $(".grade").innerText.split(": ")[1];
  renApp({ el: "p", text: query }, $(".hist-container"))
}
