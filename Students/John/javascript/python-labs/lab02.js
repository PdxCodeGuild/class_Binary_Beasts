/*

all codes are written and created by John Robson Thu Mar 18, 2021

*/

export function runLab02() {
  renApp(
    [
      { el: "h1", text: "Lab 02 - Mad Libs" },
      { el: "label", text: getText("nouns") },
      { el: "input", cl: "noun" },
      { el: "label", text: getText("emotions") },
      { el: "input", cl: "adj" },
      { el: "label", text: getText("articles of clothing") },
      { el: "input", cl: "clothing" },
      { el: "button", text: "Submit", cl: "grade-btn" },
    ],
    $("main")
  );

  $(".grade-btn").onclick = getValues;
}

function getValues() {
  let validation;

  $$("input").forEach((input) => {
    if (input.value === "") validation = false;
  });

  if (!validation)
    renApp(
      { el: "p", cl: "error", text: "Please fill out all fields." },
      $("main")
    );

  const nounsList = $(".noun").value.split(","),
    adjList = $(".adj").value.split(","),
    clothingList = $(".clothing").value.split(",");

  printLyrics(nounsList, adjList, clothingList);
}

function printLyrics(nouns, adjs, clothes) {
  const h2 = ren({ el: "h2", text: "Results: " }),
    pText = `Be our ${rand(nouns)}
    Be our ${rand(nouns)}
    Turning 60 is ${rand(adjs)}
    tighten up your bow tie around your neck and wear your favorite ${rand(
      clothes
    )}`,
    p = ren({ el: "p", text: pText }),
    p2 = ren({ el: "p", text: "Refresh page to play again." });

  clear($("main"));
  app([h2, p, p2], $("main"));
}

function getText(word) {
  return "Please enter some " + word + " separated by a comma";
}
