# Regex

Regex (regular expressions) are used to define search patterns. You can read more about regex in JavaScript on the [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions). Also, you can test your Regex skills [here](https://regexr.com/).

For example, how do I find only numbers that are included inside parenthesis?

```Javascript
const regex = /\(\d+\)/g
const text = "(56), (hello), ($$)"

const matches = regex.exec(text);
console.log(matches)
```

Here are some of the most common methods used With Regex (more on the MDN page linked above):

1. Make a search for a match in a string using `exec()`(example above)
2. Check whether a string includes a pattern with `test()`. It returns true or false.

```Javascript
const regex = /foo+/g //g means Global and + is 'one or more'
const text = 'table football'
const matches = regex.test(text);
console.log(matches)
```

3. Check if a string matches your pattern. `match()` will return an array containing all of the matches, including capturing groups, or null if no match is found.

```Javascript
const regex = /[A-Z]/g; //Matches any characters between A and Z. This is case sensitive.
const text =  'The quick brown fox jumps over the lazy dog. It barked.'
const matches = text.match(regex);
console.log(matches)
```

A variation could be:

```Javascript
const regex = /[A-Z]\w+/g; //Matches any words that begin with a lettern between A and Z. This is case sensitive.
const text =  'The Quick brown Fox jumps over the lazy dog. It barked.'
const matches = text.match(regex);
console.log(matches)
```

4. Make a search for a match in a string, and replace the matched substring with a replacement substring using `replace()`

```Javascript
const regex = /Lorem Ipsum/g;

const text =  "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

const matches = text.replace(regex, 'ice cream');
console.log(matches)
```

# Form Validation

There are two ways of doing form validation. You can either use [HTML5's pattern attribute](../../2%20HTML%20+%20CSS/docs/12%20-%20HTML%20Forms.md#the-pattern-attribute), or you can use JavaScript. While the `pattern` attribute is quick and easy, JavaScript gives you more control.

It's important to note that regular expressions are _not_ a standardized language. Each implementing language does them slightly differently. Regular expressions in JS are slightly different than those in Python. To write them out in JS, use a regexp literal, which is the pattern surrounded by forward slashes `/`.

Below is an example using input fields.

```html
<input id="username_input" type="text" />
<span id="username_info" style="display:none;color:red;"
  >username must be between 1 and 15 lowercase characters</span
>
<script>
  const username_input = document.querySelector("#username_input");
  const username_info = document.querySelector("#username_info");

  // this event is triggered whenever the value in the input field is changed
  username_input.addEventListener("input", function () {
    // define a regex pattern that checks for a set of charachters (excluding spaces and numbers) between 1 and 15 letters.
    //^abc$ defines the start / end of the string.
    const pattern = /^[a-z]{1,15}$/;

    // if the pattern doesn't the input value, indicate the error
    if (!pattern.test(this.value)) {
      this.style.outline = "1px solid red";
      username_info.style.display = "inline";
    } else {
      this.style.outline = "1px solid black";
      username_info.style.display = "none";
    }
  });

  //here's a pattern for 1-15 characters, including spaces, symbols and numbers 
  // const pattern = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-\s]{1,15}$/; 
</script>
```
