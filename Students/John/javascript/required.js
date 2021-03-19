/*

all codes are written and created by John Robson Thu Mar 18, 2021

*/

import { runLab02 } from "./lab02.js";

const labs = ["Lab 02"];
const links = [runLab02];
const body = document.body;
generateLabInput();
const main = document.createElement("main");
body.append(main);

const select = document.querySelector("select");

select.onchange = renderLab;

function renderLab() {
  const lab = document.querySelector("select").value;
  if (lab == NaN) while (main.firstChild) main.firstChild.remove();
  else links[parseInt(lab)]();
}

function generateLabInput() {
  const section = document.createElement("section");

  const label = document.createElement("label");
  label.className = "nav-label";
  label.innerText = "Choose a Lab:";

  const select = document.createElement("select");

  const blankOption = document.createElement("option");
  blankOption.value = null;
  blankOption.innerText = "";

  select.append(blankOption);

  labs.forEach((lab, i) => {
    const option = document.createElement("option");
    option.value = i;
    option.innerText = lab;
    select.append(option);
  });

  section.append(label, select);
  body.append(section);
}
