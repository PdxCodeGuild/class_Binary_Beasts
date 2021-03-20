/*

all codes are written and created by John Robson Fri Mar 19, 2021

*/

export function runLab11() {
  renApp(
    [
      { el: "h1", text: "Lab 11 - Change Maker" },
      { el: "h2", cl: "data", text: "Data: [ " + data.join(", ") + " ]" },
      { el: "button", cl: "horizontal", text: "Draw Horizontal" },
      { el: "button", cl: "vertical", text: "Draw Vertical" },
      { el: "div", cl: "graph" },
    ],
    $("main")
  );

  $(".horizontal").onclick = drawHorizontal;
  $(".vertical").onclick = drawVertical;
}