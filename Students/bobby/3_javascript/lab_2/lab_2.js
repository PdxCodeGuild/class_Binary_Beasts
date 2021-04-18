
const todos = document.querySelector(".todos");
const input = document.querySelector(".todo-input");
const triggerAdd = document.getElementById("add");
const triggerCompleted = document.querySelector(".completed");
const triggerli = document.querySelector(".todos");
const completed = document.querySelector(".completed");
const triggerRemove = document.getElementById("remove")

triggerAdd.addEventListener("click", function() { // event listener by a click that targets the add button
    const li = document.createElement("li"); // Variable li is creating a list element
    li.innerText = input.value // list element is coming from the input value
    input.value = "" // This removes the text from the field
    todos.append(li) // This appends the list todos
});

triggerli.addEventListener("click", function(event) { // event listener by a click that targets the list element in todos
    completed.appendChild(event.target) // this takes the list element in todos and appends it to completed
});

triggerRemove.addEventListener("click", function(event) { // event listener by a click that targets the remove button
    const firstOftheList = todos.children[0] // New variable to target the todos list at element 0
    todos.removeChild(firstOftheList) // removes the element in the todos list at element 0
});
