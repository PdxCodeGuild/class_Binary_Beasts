
# Fundamentals

You can read more about JavaScript syntax on the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar).

## Naming, indentation

Javscript does not care about indentation. Be organized and follow the same indentation structure that you observed with Python. This will improve code readability. 

It's convention to use camelCase. All names start with a letter:

```Javascript

const goingToShop = 'fun!'
const price = 19.90;
const tax = 0.20;

```


## Declaring Variables

There are three ways to declare variables: `var`, `let` and `const`. The only difference between `var` and `let` is that `let` has a more limited scope. In general, `let` is preferable, unless you your code needs to be compatible with older browsers.

```javascript
if (2 < 10) {
    var x = 10; // scope extends beyond the if
    const y = 11; // scope is limited to the if
}
console.log(x); // 10
console.log(y); // error

for (var x=0; x<10; ++x) {}
alert(x); // 10

for (let y=0; y<10; ++i) {}
alert(y); // error
```

Variables declared `const` cannot change value, this is advantageous for declaring constants.

```javascript
const pi = 3.1415;
pi += 1 // error
```


## Data Types

```javascript
const a = 5; // number
const b = 10.4; // number
const c = "hello!"; // string
const d = true; // boolean
const e = null; // null
const f = undefined; // undefined

// arrays are like python lists
const fruits = ["apple", "bananana", "pear"];
fruits[0] = 'cherry'; // set the element at that position
fruits.push('pomegranate'); // add a new element

// objects are like Python dictionaries
const person = {
    firstName:"John",
    lastName:"Doe",
    age:46
};
person.age += 1;
person['age'] += 1;
```

To convert between types, use `parseInt`, `parseFloat` and `toString`.

```javascript
const x = parseInt('4');
const y = parseFloat('4.2');
const z = x.toString();
```


## Comments

Use `//` for line-comments, `/* ... */` for block-comments.

```javascript
// this is a line comment
const x = 10; // this is another line comment
/* this is a block comment
which can span multiple lines*/
```


## Input

An easy way to get input from a user is `prompt`, a function which takes the text to display as a parameter and returns whatever the user entered.

```javascript
const name = prompt("Please enter your name");
alert("Hello " + name + "! How are you today?");
```

You can also use `input` elements.

```html
<input id="name_input" type="text"/>
<script>
    const name_input = document.querySelector('#name_input');
    const name_value = name_input.value;
    alert(name_value);
</script>
```


## Output

Below are three simple ways of getting output to the user.

The `alert` function shows the user text in the form of a popup.

```javascript
alert('Hello World!');
```

The `console.log` function will print the parameter in the developer console (F12). If the parameter is an object, you'll be able to look through the data much more easily than if it were one giant string.

```javascript
console.log("Hello World!");
```

The `document.write(s)`  function will replace all existing HTML on the page with whatever you give it (which can be a string containing HTML)

```javascript
document.write('<span>Hello World!</span>');
```

