/*

all codes are written and created by John Robson Thu Mar 18, 2021

*/

export function runLab02() {
  const main = document.querySelector("main");
  while (main.firstChild) main.firstChild.remove();

  const h1 = document.createElement("h1");
  h1.innerText = "Lab02 - Mad Libs";

  const nounLabel = document.createElement("label");
  nounLabel.innerText = "Please enter some nouns separated by a comma";
  const nounInput = document.createElement("input");
  nounInput.className = "noun";
  nounInput.type = "text";

  const adjLabel = document.createElement("label");
  adjLabel.innerText = "Please enter some emotions separated by a comma";
  const adjInput = document.createElement("input");
  adjInput.className = "adj";
  adjInput.type = "text";

  const clothingLabel = document.createElement("label");
  clothingLabel.innerText =
    "Please enter some articles of clothing separated by a comma";
  const clothingInput = document.createElement("input");
  clothingInput.className = "clothing";
  clothingInput.type = "text";

  const submitButton = document.createElement("button");
  submitButton.innerText = "Submit";

  main.append(
    h1,
    nounLabel,
    nounInput,
    adjLabel,
    adjInput,
    clothingLabel,
    clothingInput,
    submitButton
  );

  submitButton.onclick = getValues;
}

function getValues() {
  const main = document.querySelector("main");
  const nounInput = document.querySelector(".noun");
  const adjInput = document.querySelector(".adj");
  const clothingInput = document.querySelector(".clothing");
  const inputs = document.querySelectorAll("input");

  let validation;
  inputs.forEach((input) => {
    if (input.value === "") validation = false;
  });

  if (!validation) {
    const p = document.createElement("p");
    p.className = "error";
    p.innerText = "Please fill out all fields.";
    main.append(p);
  }

  const nounsList = nounInput.value.split(","),
    adjList = adjInput.value.split(","),
    clothingList = clothingInput.value.split(",");

  printLyrics(nounsList, adjList, clothingList);
}

function printLyrics(nouns, adjs, clothes) {
  const main = document.querySelector("main");
  const h2 = document.createElement("h2");
  h2.innerText = "Results:"
  const p = document.createElement("p");
  p.innerHTML = `Be our ${getRandom(nouns)}<br />
    Be our ${getRandom(nouns)}<br />
    Turning 60 is ${getRandom(adjs)}<br />
    tighten up your bow tie around your neck and wear your favorite ${getRandom(
        clothes
    )}`;

  const p2 = document.createElement("p");
  p2.innerText = "Refresh page to play again";

  while (main.firstChild) main.firstChild.remove();
  main.append(h2, p, p2);
}

function getRandom(list) {
  let i = Math.round(Math.random() * (list.length - 1));
  return list[i];
}
