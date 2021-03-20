/*

all codes are written and created by John Robson Fri Mar 19, 2021

*/

const tokens = ["Rock", "Paper", "Scissors"],
  wins = [
    [0, 2],
    [1, 0],
    [2, 1],
  ];

export function runLab07() {
  renApp(
    [
      { el: "h1", text: "Lab 07 - Rock, Paper, Scissors" },
      { el: "button", text: "Rock", cl: "rps rock" },
      { el: "button", text: "Paper", cl: "rps paper" },
      { el: "button", text: "Scissors", cl: "rps scissors" },
    ],
    $("main")
  );

  $$("button").forEach((b) => (b.onclick = registerClick));
}

const registerClick = (e) => {
  const user = e.target.innerText;
  const comp = rand(tokens);
  limit($$(".rps-result"), 5)

  status = "";
  if (user === comp) status = "Tie!";
  else {
    const result = [tokens.indexOf(user), tokens.indexOf(comp)];
    status = false;
    wins.forEach((w) => {
      if (equals(w, result)) status = true;
    });

    if (status.toString() === "true") status = "You win!";
    else status = "You lose!";
  }

  let sign = "";
  if (status === "Tie!") sign = "=";
  else sign = status === "You win!" ? ">" : "<";
  const score = `${user} ${sign} ${comp}: ${status}`;
  renApp({ el: "p", cl: "rps-result", text: score }, $("main"));
};
