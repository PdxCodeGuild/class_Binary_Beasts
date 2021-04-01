/*

all codes are written and created by John Robson Fri Mar 19, 2021

*/

const data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9];

export function runLab10() {
  renApp(
    [
      { el: "h1", text: "Lab 10 - Peaks and Valleys" },
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

const drawHorizontal = () => {
  clear($(".graph"));
  let bar = 0;
  data.forEach((d) => {
    if (d > bar) bar = d;
    renApp(
      { el: "div", cl: "line", text: d + ": " + build("X", d, " ", bar, "O") },
      $(".graph")
    );
  });
};

const drawVertical = () => {
  clear($(".graph"));
  let h = Math.max(...data),
    buf = "";
  while (h > -1) {
    let bar = 0;
    data.forEach((d) => {
      if (d > bar) bar = d;
      if (h === 0) buf += d + " ";
      else if (d >= h) buf += "X ";
      else if (bar >= h) buf += "O ";
      else buf += "  ";
    });
    buf += "\n";
    h--;
  }
  renApp({ el: "pre", text: buf, cl: "line" }, $(".graph"));
};
