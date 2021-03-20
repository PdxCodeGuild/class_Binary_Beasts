/*

all codes are written and created by John Robson Thu Mar 18, 2021

*/
import { runLab02 } from "./lab02.js";
import { runLab03 } from "./lab03.js";
import { runLab04 } from "./lab04.js";

const labs = ["Lab 02", "Lab 03", "Lab 04"];
const links = [runLab02, runLab03, runLab04];
const body = document.body;
generateLabInput();
renApp({ el: "main" }, body);

$("select").onchange = renderLab;

function renderLab() {
  const lab = $("select").value;
  clear($("main"));
  if (lab !== "") links[parseInt(lab)]();
}

function generateLabInput() {
  const section = ren({ el: "section" }),
    label = ren({ el: "label", cl: "nav-label", text: " Choose a Lab:" }),
    select = ren({ el: "select" });
    renApp({ el: "option" }, select)

  labs.forEach((lab, i) => {
    renApp({ el: "option", text: lab, value: i }, select)
  });


  app([label, select], section);
  app(section, body)
}
