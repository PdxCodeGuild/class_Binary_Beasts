/*
Theo Rafael Cocco
Sunday April 18, 2021
Lab 2, Todo List
Last Updated Wednesday April 21, 2021
*/

// Version 1

/* 
const input = document.querySelector("input"),
  add = document.querySelector(".add"),
  todo = document.querySelector(".incomplete"),
  done = document.querySelector(".complete"),
  remove = document.querySelector(".remove");

add.addEventListener("click", () => {
  const li = document.createElement("li");
  li.className = "todo";
  li.innerText = input.value;
  todo.append(li);
  input.value = "";
});

remove.addEventListener("click", () => {
  const li = document.querySelector(".todo");
  if (input.value == li.innerText) {
    li.remove();
    input.value = "";
  }
});

document.addEventListener("click", (event) => {
  let list = document.querySelectorAll(".todo");
  list.forEach((t) => {
    if (event.target == t) {
      const x = event.target;
      x.className = "completed";
      x.style.color = "gray";
      x.style.textDecoration = "line-through";
      done.append(x);
    }
  });
});
 */

// Version 2 JQuery

$(".add").click(() => {
  const li = $("<li>", { class: "todo" });
  $(li).text($("input").val());
  $(".incomplete").append(li);
  $("input").val("");
});

$(".remove").click(() => {
  // $("li").each(() => {
  //   if ($("input").val() == $("li").text()) {
  //     $("li").remove();
  //     $("input").val("");
  //   }
  // });
  let children = $(".incomplete").find("li");
  children[0].remove();
});
