// jquery to add values to a list
$("#btn-list").on('click', function(){
    const li = "<li>" + $("#text-field").val() + "</li>"
    console.log(li)
    $('#incompleteText').append(li)
})
$("#incompleteText").on('click', function(){
    const li = "<li>" + $("#text-field").val() + "</li>"
    let children = $('#incompleteText').find("li")
    children[0].remove()
    console.log(children)
    $('#completedText').append(li)
    $("#completedText").css({"text-decoration": "line-through"})
})