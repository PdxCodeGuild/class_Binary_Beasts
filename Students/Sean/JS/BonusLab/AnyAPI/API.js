quote = document.getElementById("quote")
btn = document.getElementById("get")

btn.addEventListener("click", function(){
  fetch("https://type.fit/api/quotes")
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    rand = Math.floor(Math.random() * data.length)
    quote.innerHTML = data[rand].text
  });
})