$("#addBtn").on("click", function () {
    let li = "<li>" + $("#addItem").val() + '<button type="button" class="clearBtn">X</button>' + '<button type="button" class="check">D</button>' + "</li>";
    
    $("#toDoList").append(li)

    $("li").on("click", function (event) {
        let listItem = $(this);
        if(event.target.className == "clearBtn"){
            listItem.remove()
        }else if(event.target.className == "check"){
            $("#completed").append(listItem)
        }
    });

    $("#addItem").val('');
});

$("#clrBtn").on("click", function () {
    $("#toDoList").html('')
    $("#completed").html('')
})

