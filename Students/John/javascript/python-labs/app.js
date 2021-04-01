/*

all codes are written and created by John Robson Thu Mar 18, 2021

*/

import { runLab02 } from "./lab02.js";
import { runLab03 } from "./lab03.js";
import { runLab04 } from "./lab04.js";
import { runLab05 } from "./lab05.js";
import { runLab06 } from "./lab06.js";
import { runLab07 } from "./lab07.js";
import { runLab08 } from "./lab08.js";
import { runLab09 } from "./lab09.js";
import { runLab10 } from "./lab10.js";
import { runLab11 } from "./lab11.js";

const labs = [
  "Lab 02",
  "Lab 03",
  "Lab 04",
  "Lab 05",
  "Lab 06",
  "Lab 07",
  "Lab 08",
  "Lab 09",
  "Lab 10",
  "Lab 11",
];
const links = [
  runLab02,
  runLab03,
  runLab04,
  runLab05,
  runLab06,
  runLab07,
  runLab08,
  runLab09,
  runLab10,
  runLab11,
];
const body = document.body;
generateLabInput();
renApp({ el: "main" }, body);

$("select").onchange = renderLab;

function renderLab() {
  clear($("main"));
  if ($("select").value !== "") links[parseInt($("select").value)]();
}

function generateLabInput() {
  const section = ren({ el: "section" }),
    label = ren({ el: "label", cl: "nav-label", text: " Choose a Lab:" }),
    select = ren({ el: "select" });
  renApp({ el: "option" }, select);

  labs.forEach((lab, i) => {
    renApp({ el: "option", text: lab, value: i }, select);
  });

  app([label, select], section);
  app(section, body);
}
