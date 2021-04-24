

$("btn-list").on('click', function(){
    const li = "<li>" + $("#text-field").val() + "</li>"
    $('#list').append($li)
})