

document.getElementById("add-to-list").addEventListener("click",function(){
    console.log("entered")
    ul = document.getElementById("todo-list");
    li = document.createElement("li");
    li.appendChild(document.createTextNode(document.getElementById("task").value))
    console.log(document.createTextNode(document.getElementById("task").value))
    ul.appendChild(li)
    task = document.getElementById("task")
    task.value = ""
})


document.getElementById("remove-from-list").addEventListener("click",function(){
    listItems = document.getElementById("todo-list")
    listItems.removeChild(listItems.lastElementChild)
})


document.getElementById("todo-list").addEventListener("click",function(event){
    listItems = document.getElementById("todo-list")
    completedItem = document.createElement("li")
    completedItem.innerHTML = event.target.innerHTML
    event.target.remove()
    completedItem.style.textDecorationLine = "line-through"
    completedList = document.getElementById("completed-item-list")
    completedList.appendChild(completedItem)
})