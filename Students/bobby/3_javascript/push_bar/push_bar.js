const grow = document.getElementById("container");
const bar = document.getElementById("bar");
const triggerButton = document.getElementById("button");
let currentAlternateWidth = grow.style.width;
let currentWidth = grow.offsetWidth;

triggerButton.addEventListener("click", function () {
  currentWidth += 50;
  grow.style.width = `${currentWidth}px`;
  console.log(grow.style.width);
});

setInterval(function () {
  if (currentWidth > 150) {
    currentWidth -= 50;
    grow.style.width = `${currentWidth}px`;
    console.log("interval ran", grow.style.width);
  }
}, 1000);
