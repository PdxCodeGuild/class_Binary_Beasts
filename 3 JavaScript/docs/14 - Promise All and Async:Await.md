## Promise All

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
