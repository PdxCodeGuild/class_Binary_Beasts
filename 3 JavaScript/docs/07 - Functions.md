

# Functions

Function allow us to isolate sections of code. You can learn more about functions [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Build_your_own_function).

There are two ways to define functions in JavaScript. You can declare a function:

```JavaScript
function add(a, b) {
    return a + b;
}
console.log(add(5, 2));
```

You can also assign an anonymous function to a variable:

```JavaScript
const add = function(a, b) {
    return a + b;
}; // this is a statement, and needs a semi-colon
console.log(add(5, 2));
```

When we declare a function, it's automatically moved to the top of the script when the script is run. This means it can be called before it's declared.

```javascript

// ok
console.log(add(5, 2));
function add(a, b) {
    return a + b;
}

// crashes
console.log(add(5, 2));
const add = function(a, b) {
    return a + b;
};
```

## Default Arguments

```javascript
function add(a, b=1) {
    return a + b;
}
add(5, 2); // 7
add(5); // 6
```


## Passing Functions as Parameters

It's very common to pass a function as a parameter to another function. You can see an example of this in [element.addEventListener()](10%20-%20Events.md), [setTimeout()](12%20-%20Timing.md), and [windowRequestAnimationFrame()](13%20-%20Canvas%20Drawing.md). The example below performs an operation on each element of an array.

```javascript
const nums = [1, 2, 3];

//defining the function
function perform_operation(arr, f) {
  for (let i=0; i < nums.length; ++i) {
    nums[i] = f(nums[i]);
  }
  return nums
}
//argument function
function doublers(x){
  return x * x
}
//calling the function
perform_operation(nums, doublers);
alert(nums); 
```