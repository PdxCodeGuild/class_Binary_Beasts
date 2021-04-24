## Promises

A Promise is an object representing the eventual completion or failure of an asynchronous operation. What does asynchronous mean?

Javascript is a single threaded language. This means that it executes code in the order in which it was written, and it must finish executing a piece of code before moving onto the next. For instance, take a look at this code:

```javascript
console.log(1);
console.log(2);
console.log(3);
```

As expected, the code above will be executed in the order in which is written or _synchronously_. This represents a limitation, especially working with HTTP requests. Let's imagine that you are visiting a page and in the background there's an HTTP request to the server that is taking too long to run. Imagine that the browser can load all the elements in the page, including buttons, text, images only after that the HTTP request has finished running. This would cause the visitor to leave and would be a terrible user experience.

Promises are one of the methods that Javascript uses to solve this problem, they make code run _asynchronously_. That's how you write a promise:

```javascript
const promise = new Promise(function (resolve, reject) {
  // do a thing, possibly async, then…

  if (2 + 3 == 4) {
    resolve("Stuff worked!");
  } else {
    reject(Error("It broke"));
  }
});
```

The promise constructor takes one argument, a callback with two parameters, resolve and reject. Do something within the callback, perhaps async, then call resolve if everything worked, otherwise call reject. In this case the promise will be rejected because 4 isn't equal to 2+3.

Here's how you would use that promise:

```javascript
promise
  .then(function (result) {
    console.log(result); // "Stuff worked!"
  })
  .catch(function (err) {
    console.log(err); // Error: "It broke"
  });
```

_then()_ takes two arguments, a callback for a success case, and another for the failure case. Both are optional, so you can add a callback for the success or failure case only.

The code below is a good example of how promises allow asynchronous code to run:

```javascript
console.log("Hello Promise");
const p = new Promise((resolve, reject) => {
  console.log("Promise started working");
  console.log("Promise is doing some important work…");
  console.log("Promise has completed, about to resolve");
  resolve("Promise resolved");
});
p.then((message) => {
  console.log("Resolved!!!");
});
console.log("Normal work flow");
let count = 0;
for (let i = 0; i < 10000; i++) {
  count += 1;
}
console.log("Count: ", count);
setTimeout(() => {
  console.log("Timed out");
}, 0);
console.log("Goodbye dear Promise");
```

Let's take a closer look to a real API call with Promises using XMLHttpRequest (often abbreviated to "XHR"). These type of syntax has been replaced by Fetch.

```html
<img id="demo" />

<script>
  const promise = new Promise(function (resolve, reject) {
    const req = new XMLHttpRequest();
    req.open("GET", "https://api.thecatapi.com/v1/images/search?size=full");
    req.onload = function () {
      if (req.status == 200) {
        const img = JSON.parse(this.responseText);
        resolve(img);
      } else {
        reject("error" + req.status);
      }
    };
    req.send();
  });

  promise
    .then((result) => {
      img = result[0].url;
      displayImage(img);
    })
    .catch((error) => {
      console.error("Catch Method: ", error);
    });

  function displayImage(some) {
    let img;
    document.getElementById("demo").src = some;
  }
</script>
```

Here's a more modern way to handle API calls using promises with fetch:

```javascript
fetch("https://jsonplaceholder.typicode.com/todos/1")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => {
    console.error("There has been a problem with your fetch operation:", error);
  });
```

Axios is preferred over fetch for its wider support. Axios is a popular, promise-based HTTP client that sports an easy-to-use API and can be used in both the browser and Node. For more information, consult the document n.18 _Axios_

## Promises vs async callbacks

- You can chain multiple async operations together using multiple .then() operations, passing the result of one into the next one as an input. This is much harder to do with callbacks, which often ends up with a messy ["pyramid of doom" (also known as callback hell).](https://i.stack.imgur.com/oDSVD.png)

- Promise callbacks are always called in the strict order they are placed in the event queue.
- Error handling is much better — all errors are handled by a single .catch() block at the end of the block, rather than being individually handled in each level of the "pyramid".
