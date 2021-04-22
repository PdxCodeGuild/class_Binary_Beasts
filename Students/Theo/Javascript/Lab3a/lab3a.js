const h1 = document.querySelector(".time"),
  start = document.querySelector(".start"),
  st0p = document.querySelector(".stop"),
  lap = document.querySelector(".lap"),
  sw = document.querySelector(".stopwatch");
var timer,
  x = 1;

sw.innerText = "0:0:0:0";

setInterval(() => {
  const t = new Date().toLocaleTimeString();
  h1.innerText = t;
}, 1000);

start.addEventListener("click", () => {
  const d = new Date();
  let i = 0;
  sw.innerText = d.setHours(0, 0, 0, 0);
  timer = setInterval(() => {
    d.setHours(0, 0, 0, (i += 100));
    sw.innerText = `${d.getHours()}:${d.getMinutes()}:${d.getSeconds()}:${
      d.getMilliseconds() / 100
    }`;
  }, 100);
});

st0p.addEventListener("click", () => clearInterval(timer));

lap.addEventListener("click", () => {
  const li = document.createElement("li");

  li.innerText = `Lap ${x}: ${sw.innerText}`;
  document.body.append(li);
  x++;
});
