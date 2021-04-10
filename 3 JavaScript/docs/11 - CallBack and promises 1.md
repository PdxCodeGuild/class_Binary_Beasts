## Call Back Functions

A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.

```javascript
function greeting(name) {
  alert("Hello " + name);
}

function processUserInput(callback) {
  const name = prompt("Please enter your name.");
  callback(name);
}

//passing the function greeting into processUserInput
processUserInput(greeting);
```

Because callback functions are functions passed into other functions, you can see them in the doc n.16 with map, sort, reduce and filter.

Here's onother clear example of a callback function:

```javascript
const arr = ['a', 'b', 'c', 'd', 'e'];

function printItem(item, index) {
  console.log(`index: ${index} value: ${item}`);
}
arr.forEach(printItem);
```

The _forEach()_ method executes a provided function once for each array element. So, for each element, we are running the function _printItem_

Compare the above function with the one below:

```Javascript
const arr = ['a', 'b', 'c', 'd', 'e'];

function printItem(item) {
  for (let i =0; i < item.length; i++){
   console.log(`index: ${i} value: ${item[i]}`}
}
printItem(arr)
```

Let's make another example:

```html
<button id="btn">Save</button>
<script>
  function btnClicked() {
    // do something here
  }
  const btn = document.querySelector("#btn");
  btn.addEventListener("click", btnClicked);
</script>
```

Which would be the equivalent of:

```javascript
const btn = document.querySelector("#btn");
btn.addEventListener("click", function () {
  // do something here
  //using an anonimous function as well
});
```

Here's an example of a callback function to change the color of squares:

```html
<div id="red"></div>
<div id="blue"></div>
<div id="yellow"></div>

<style>
  div {
    width: 500px;
    height: 500px;
    border: 1px solid black;
  }
</style>

<script>
  function myElement(elem, color) {
    document.getElementById(elem).style.backgroundColor = color;
  }

  function changeColor(elem, color) {
    myElement(elem, color);
  }

  changeColor("red", "red");
  changeColor("blue", "blue");
  changeColor("yellow", "yellow");
</script>
```

You would use a callback function to work with asynchronous operations. In the example below we simulate getting data from a server.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>repl.it</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <script src="script.js"></script>
  </body>
  <script>
    const posts = [
      { id: 1, title: "blog 1" },
      { id: 2, title: "blog 2" },
    ];

    function getPosts() {
      setTimeout(function () {
        let result = "";
        posts.forEach(function (blog) {
          result += `<li>${blog.title}</li>`;
        });
        document.body.innerHTML = result;
      }, 1000);
    }

    function addPost(post) {
      setTimeout(function () {
        posts.push(post);
      }, 2000);
    }
    addPost({ id: 3, title: "blog 3" });
    getPosts();
  </script>
</html>
```

In the example above the server returned data before we could add our new blog post. By that time, the DOM already rendered. We could fix it using a callback function:

```Javascript

 function addPost(post, callback) {
      setTimeout(function(){
        posts.push(post);
        callback()
      }, 2000);
    }
    addPost({ id: 3, title: "blog 3" }, getPosts);

```

## Promises

A Promise is an object representing the eventual completion or failure of an asynchronous operation.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>repl.it</title>
    <link href="style.css" rel="stylesheet" type="text/css" />
  </head>

  <body>
    <script>
      const posts = [
        { id: 1, title: "blog 1" },
        { id: 2, title: "blog 2" },
      ];

      function getPosts() {
        setTimeout(function () {
          console.log("adding post");
          let result = "";
          posts.forEach(function (blog) {
            result += `<li>${blog.title}</li>`;
          });
          document.body.innerHTML = result;
        }, 1000);
      }

      function addPost(post) {
        return new Promise(function (resolve, reject) {
          setTimeout(function () {
            console.log("pushing post");
            posts.push(post);
            const error = false;
            if (!error) {
              resolve();
            } else {
              reject("did not get data");
            }
          }, 2000);
        });
      }
      addPost({ id: 3, title: "blog 3" })
        .then(getPosts)
        .catch(function (error) {
          console.log(error);
        });
    </script>
  </body>
</html>
```
