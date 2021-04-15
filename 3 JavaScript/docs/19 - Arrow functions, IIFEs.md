## Arrow functions

An arrow function expression is a compact alternative to a traditional function expression, but is limited and can't be used in all situations. You can read more [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

Let's take a look at a traditional anonymous function expression:

```Javascript
function example (a){
  return a + 100;
}
```

With an arrow function we can remove the keyword `function` the `return` statement because it's implied, the curly brackets and the argument parenthesis. We get the following:

```Javascript
const example = (a) => a + 100;
```

However, if you have multiple arguments, or no arguments, you'll need to add the parenthesis around the argument:

```Javascript
function mySum (a,b){
  return a + b + 100;
}
```
becomes:

```Javascript
const mySum = (a, b) => a + b + 100;
```

If you have multiple arguments:

```Javascript
const a = 4;
const b = 2;
function anotherSum (){ 
  return a + b + 100;
}
```

It will become:


```Javascript
const a = 4;
const b = 2;
const anotherSum = () => a + b + 100;

```

If the body requires additional lines of processing, you'll need to re-introduce brackets with the `return`

```Javascript
// Traditional Function
function withBrackets (a, b){
  const chuck = 42;
  return a + b + chuck;
}
 
// Arrow Function
const withBrackets = (a, b) => {
  const chuck = 42;
  return a + b + chuck;
}
```

## IIFE

An IIFE (Immediately Invoked Function Expression) is a JavaScript function that runs as soon as it is defined.

```Javascript
(function () {
    const name = "Barry"; 
    return name; 
})(); 
// Immediately creates the output: 
// result: "Barry"
```