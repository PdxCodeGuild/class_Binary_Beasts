  axios.post('https://jsonplaceholder.typicode.com/posts', {
    firstName: 'Finn',
    lastName: 'Williams'
  })
  .then((response) => {
    console.log(response);
  }, (error) => {
    console.log(error);
  });

  document.getElementById("submit").addEventListener("click", function(event){
    event.preventDefault()
  });