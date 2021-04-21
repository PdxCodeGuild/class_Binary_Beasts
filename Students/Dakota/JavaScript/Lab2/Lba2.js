const text_field = document.getElementById("user_input");
const output = document.getElementById("output");
const trigger = document.getElementById("trigger");
trigger.addEventListener("click", function () {
    console.log(text_field.value);
    output.innerText = text_field.value;
});
const addTrigger = document.getElementById("addTrigger");
addTrigger.addEventListener("click", function () {
    var text = "";
    var inputs = document.querySelectorAll("input[type=text]");
        for (var i = 0; i < inputs.length; i++) {
            text += inputs[i].value;
        }
    var li = document.createElement("li");
    var node = document.createTextNode(text);
    li.appendChild(node);
    document.getElementById("list").appendChild(li);
    const remove = document.getElementById("remove");
    const removeTrigger = document.getElementById("removeTrigger");
    removeTrigger.addEventListener("click", function () {
        li.remove("li")
    });
});
const complete = document.getElementById("complete");
const completeTrigger = document.getElementById("completeTrigger");
completeTrigger.addEventListener("click", function () {
    var text = "";
    var inputs = document.querySelectorAll("input[type=text]");
    for (var i = 0; i < inputs.length; i++) {
        text += inputs[i].value;
    }
    var li = document.createElement("li");
    var node = document.createTextNode(text);
    li.appendChild(node);
    document.getElementById("completedList").appendChild(li);
});
