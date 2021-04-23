$("#add").on("click", function () {
  const $li = "<li>" + $(".todo-input").val() + "</li>";
  $(".todo-input").val("");
  $(".todos").append($li);
});

$(".todos").on("click", function (event) {
  $(".completed").append(event.target);
});

$("#remove").on("click", function () {
  const firstOftheList = $(".todos").children();
  firstOftheList[0].remove()
});
