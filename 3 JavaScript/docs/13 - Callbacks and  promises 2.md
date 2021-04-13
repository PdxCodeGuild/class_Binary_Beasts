## Promise All

Promise All allows you to chaing promises and resolve them all at once.

```Javascript
const promise1 = Promise.resolve(3);
const promise2 = 42;
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'foo');
});

Promise.all([promise1, promise2, promise3]).then((values) => {
  console.log(values);
});
// expected output: Array [3, 42, "foo"]

```

Let's do a real case example. Let's say that you need to get data from 3 different APIs. Instead of filling the page with `.then(s)` you would use `Promise.all`:

```Javascript

const urls = [
  'https://jsonplaceholder.typicode.com/todos/1',
  'https://jsonplaceholder.typicode.com/todos/2',
  'https://jsonplaceholder.typicode.com/todos/3'
];

// map every url to the promise of the fetch
const requests = urls.map(function(urls) {
  return fetch(urls).then(function(data){
    return data.json()
  })
});

// Promise.all waits until all jobs are resolved
Promise.all(requests)
  .then(function (data) {
    console.log(data);
  }).catch(function (error) {
    console.log(error);
  });
```

You can shorten it using arrow functions

```Javascript
Promise.all(requests)
  .then((data => {
    console.log(data);
  })).catch((error) => {
    console.log(error);
  });
```

## Async / Await

Async/await is just syntax sugar built on top of promises, so they can be written in a cleaner style, avoiding the need to explicitly configure promise chains.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
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

      async function getAll() {
        await addPost({ id: 3, title: "blog 3" });
        getPosts();
      }

      getAll();
    </script>
  </body>
</html>
```

Let's try this out with fetch:

```Javascript

async function getTodos(){
  const response = await fetch ("https://jsonplaceholder.typicode.com/todos/1")
  const data = await response.json()
  console.log(data)
}
 getTodos()

```

Much cleaner!
