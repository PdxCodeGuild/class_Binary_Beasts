/*

all codes are written and created by John Robson Fri Mar 19, 2021

*/

let responses;

export function runLab04() {
  renApp(
    [
      { el: "h1", text: "Lab 04 - Magic 8 Ball" },
      { el: "label", text: "What question do you have?" },
      { el: "input", cl: "magic8" },
      { el: "button", text: "Submit", cl: "magic8-btn" },
    ],
    $("main")
  );

  responses = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
  ];

  $(".magic8-btn").onclick = respond;
}

const respond = () => {
  if ($(".response")) $(".response").remove();
  if ($("input").value !== "")
    renApp({ el: "p", cl: "response", text: rand(responses) }, $("main"));
  else
    renApp(
      { el: "p", cl: "response", text: "Please enter a question." },
      $("main")
    );
  $("input").value = "";
};
