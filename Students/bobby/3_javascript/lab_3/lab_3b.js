function ranNumbs() {
  const r = Math.floor(Math.random() * 255);
  const g = Math.floor(Math.random() * 255);
  const b = Math.floor(Math.random() * 255);
  return `rgb(${r}, ${g}, ${b})`;
}

const chngColor = document.getElementById("heading");
const button = document.getElementById("btn");

button.addEventListener("click", function () {
  chngColor.style.color = ranNumbs();
});
