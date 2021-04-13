# Arrays and Loops

## Arrays

Arrays are ordered, linear collections of elements. They can hold elements of any type, and elements of different types simultaneously. You can find more info [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) and [here](https://www.w3schools.com/jsref/jsref_obj_array.asp).

Array literals are designated by square-brackets and commas:

```javascript
const nums = [2, 1, 3];
const fruits = ["apple", "bananana", "pear"];
```

You can access or set an element by using its index:

```javascript
const fruits = ["apple", "bananana", "pear"];
console.log(fruits[0]); // apple
fruits[0] = "cherry";
console.log(fruits[0]); // cherry
```

Below are some common operations that can be performed on arrays.

- `length` represents the length of the array
- `push(element)` places a new element at the end
- `pop()` remove an element from the end of an array
- `unshift(element)` places an element at the beginning
- `shift()` remove an element from the beginning
- `indexOf(element)` returns the index of the given element
- `splice()` This method changes the contents of an array by removing or replacing existing elements and/or adding new elements in place.

`replace element`

```Javascript
const months = ['Jan', 'March', 'April', 'June'];
months.splice(1, 0, 'Feb');
```

`remove 1 element at index 3`

```Javascript
const myFish = ['angel', 'clown', 'drum', 'mandarin', 'sturgeon']
const removed = myFish.splice(3, 1)
```

- `join(delimeter)` turns the array into a string, with elements separated by `delimeter`
- `concat(array)` returns a **new** array which is made of elements from both arrays
- `slice(start, end)` returns an array containing a subset of the original array, starting at `start` and ending at `end`

```javascript
const animals = ["ant", "bison", "camel", "duck", "elephant"];

console.log(animals.slice(2));
// expected output: Array ["camel", "duck", "elephant"]

console.log(animals.slice(2, 4));
// expected output: Array ["camel", "duck"]
```

- `sort()` sorts an array
- `reverse()` reverses an array

## While Loops

While loops will execute their body while the given condition is true

```javascript
let i = 0;
while (i < 10) {
  console.log(i);
  i++;
}
```

## For Loops

For loops have three parts, separated by semi-colons. The first is the **initialization**, the second is the **condition** and the third is the **increment**.

```javascript
const fruits = ["apple", "banana", "pear"];
fruits.push("cherry");
for (let i = 0; i < fruits.length; ++i) {
  console.log(fruits[i]);
}
console.log(fruits.indexOf("banana")); // 1
```

# for...of statement

The for...of statement creates a loop iterating over iterable objects, including: built-in String, Array, array-like objects (e.g., arguments or NodeList), TypedArray, Map, Set, and user-defined iterables.

```javascript
const array1 = ["a", "b", "c"];

for (const element of array1) {
  console.log(element);
}
```

# for...in statement

The for...in statement iterates over all enumerable properties of an object that are keyed by strings (ignoring ones keyed by Symbols), including inherited enumerable properties.

```javascript
const car = {
  engine: "honda",
  wheels: 4,
  color: "grey",
};

for (let item in car) {
  console.log("key", item, "value", car[item]);
}
```
