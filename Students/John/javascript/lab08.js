/*

all codes are written and created by John Robson Fri Mar 19, 2021

*/

let guessCount = 0,
  over = "false";

export function runLab08() {
  renApp(
    [
      { el: "h1", text: "Lab 08 - Guess The Number" },
      { el: "label", text: "Guess a number 1 - 9" },
      { el: "input", cl: "guess", type: "number", min: 1, max: 9 },
      { el: "input", cl: "comp-guess", type: "hidden" },
      { el: "h2", cl: "grade" },
      { el: "aside", cl: "history" },
      { el: "button", cl: "reset", text: "reset" },
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

  $(".guess").addEventListener("input", () => {
    checkInput($(".guess"), 1);
  });
  $(".guess").onchange = checkGuess;

  $(".comp-guess").value = randN(1, 9);
  $(".reset").onclick = reset;
}

const checkGuess = () => {
  checkValue($(".guess"), 1, 9);
  if ($(".guess").value == null || $(".guess").value === "") return;

  if (guessCount >= 5) {
    gameOver();
    return;
  }

  let status = "";

  if ($(".guess").value === $(".comp-guess").value) status = "You win";
  else
    status =
      $(".guess").value > $(".comp-guess").value ? "Too high" : "Too low";

  guessCount++;
  addToHistory(status);
  if (status === "You win") over = "true";
  if (guessCount >= 5) {
    gameOver();
    return;
  }
};

const reset = () => {
  checkValue($(".guess"), 1, 9);
  clear($(".hist-container"));
  $(".guess").value = "";
  guessCount = 0;
  over = "false";
};

const addToHistory = (status) => {
  if (over === "true") return;
  limit($$(".hist-item"), 5);

  $(".grade").innerText.split(": ")[1];

  let query = `${$(".guess").value}: ${status}`;
  renApp({ el: "p", cl: "hist-item", text: query }, $(".hist-container"));
};

const gameOver = () => {
  if (over !== "true") {
    over = "true";
    renApp(
      {
        el: "p",
        cl: "hist-item",
        text: "You Lose! Answer: " + $(".comp-guess").value,
      },
      $(".hist-container")
    );
  }
};
