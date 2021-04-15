# DOM

The Document Object Model (DOM) represents that same document so it can be manipulated.

JavaScript provides many functions to manipulate the DOM. You can find more info [here](https://www.w3schools.com/js/js_htmldom_document.asp).

In the DOM, all parts of the document are organized in a hierarchical tree-like structure consisting of parents, siblings and children. These individual parts of the document are known as nodes.

[Representation of the DOM](https://i.stack.imgur.com/ocR0a.png).

## Accessing Elements

You can access the elements of the DOM from JavaScript using several functions. You can find more info on these functions [here](https://javascript.info/searching-elements-dom).

| function                             | description                                        |
| ------------------------------------ | -------------------------------------------------- |
| `document.getElementById(id)`        | get an element with the given id                   |
| `document.getElementsByTagName(tag)` | get all elements of the given tag                  |
| `document.getElementsByName(name)`   | get all elements with the given name               |
| `document.querySelector(selector)`   | get an element that matches the given CSS selector |
| `document.querySelectorAll(pattern)` | get all elements that match the given CSS selector | Returns a NodeList containing all matching Element nodes. |

The following code demonstrates how each of these are used:

```html
<div id="mydiv" name="adiv" class="myclass"></div>
<div id="thisdiv" class="myclass"></div>
<div id="thatdiv" name="adiv"></div>

<script>
  const a = document.getElementById("mydiv");
  const bs = document.getElementsByTagName("div");
  console.log(bs.length); // 3
  Array.from(bs).map(function (item) {
    //allows you to iterate from a HTML collection list
    console.log(item);
  });
  const cs = document.getElementsByName("adiv");
  console.log(cs.length); // 2
  Array.from(cs).map(function (item) {
    //allows you to iterate from a Node list
    console.log(item);
  });
  const d = document.querySelector("#mydiv");
  const es = document.querySelectorAll(".myclass");
  console.log(es.length); // 2
</script>
```

## Setting innerText and innerHTML

You can set the value 'inside' a tag `<div>this</div>` using `innerText` and `innerHTML`. As you might guess, `innerText` is for text, `innerHTML` is for a string containing HTML.

```html
<div id="div1"></div>
<div id="div2"></div>
<script>
  let div1 = document.querySelector("#div1");
  div1.innerText = "Hello World!";

  let div2 = document.querySelector("#div2");
  div2.innerHTML = `<p><b>Hello World!</b></p>`;
</script>
```

This renders the following:

```html
<div id="div1">Hello World!</div>
<div id="div2">
  <p><b>Hello World!</b></p>
</div>
```

## Editing Attributes and Style

You can assign attributes to elements just as you'd assign attributes to objects.

```html
<div id="demo_div"></div>
<script>
  const demo_div = document.querySelector("#demo_div");
  demo_div.innerHTML = "Hello World!";
  demo_div.style.fontSize = "24px";
  demo_div.name = "demo_div";
</script>
```

This renders the following:

```html
<div id="demo_div" style="font-size:24px" name="demo_div">Hello World!</div>
```

Additionally, you may use these functions on the element to manipulate the attributes. These are necessary if you're attempting to edit 'non-standard' attributes.

- `element.setAttribute(attribute_name, value)`
- `element.getAttribute(attribute_name)`
- `element.hasAttribute(attribute_name)`
- `element.removeAttribute(attribute_name)`

```html
<h1>Hello World</h1>
<style>
  .myColor {
    color: red;
  }
</style>
<script>
  const settingAttribute = document
    .getElementsByTagName("H1")[0]
    .setAttribute("class", "myColor");

  const gettingAttribute = document
    .getElementsByTagName("H1")[0]
    .getAttribute("class");
  console.log(gettingAttribute);

  const hasAnAttribute = document
    .getElementsByTagName("H1")[0]
    .hasAttribute("class");
  console.log(hasAnAttribute);

  const remove = document
    .getElementsByTagName("H1")[0]
    .removeAttribute("class");
</script>
```

## Input Fields

Similarly, you can also access the values of input fields. You can read more about input fields [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input).

```html
<input id="user_input" type="text" />
<button id="trigger">click me</button>
<div id="output"></div>
<script>
  const text_field = document.getElementById("user_input");
  const output = document.getElementById("output");
  const trigger = document.getElementById("trigger");

  trigger.addEventListener("click", function () {
    console.log(text_field.value);
    output.innerHTML = text_field.value;
  });
</script>
```

## Creating and Adding Elements

We can also create elements from scratch.

| function                           | description                                         |
| ---------------------------------- | --------------------------------------------------- |
| `document.createElement(tag_name)` | create an element with tag `tag_name`               |
| `document.createTextNode(text)`    | create a text node containing the given text        |
| `element.appendChild(child)`       | append a child element to a parent element          |
| `element.removeChild(child)`       | remove a child element from a parent element        |
| `element.hasChild(child)`          | indicated whether the parent has a particular child |
| `element.replaceChild(child)`      | replaces a child                                    |

```html
<div id="container_div"></div>
<script>
  let btn = document.createElement("button");
  btn.style.backgroundColor = "lightblue";
  btn.style.border = "1px solid white";
  btn.innerText = "click";
  let container_div = document.getElementById("container_div");
  container_div.appendChild(btn);
</script>
```

## Find Children

```html
<ul>
  <li>rain</li>
  <li>sun</li>
  <li>snow</li>
</ul>

<script>
  //two identical ways to find children starting from the parent. This is an example of document traversal

  const ul = document.getElementsByTagName("ul");
  //because it returns an array, we have to select the index first.
  console.log(ul[0].children);

  children = document.querySelectorAll("ul li");
  console.log(children);
</script>
```
