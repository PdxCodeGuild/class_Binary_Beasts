# jQuery

[jQuery](https://jquery.com/) is a JavaScript library that can make general DOM manipulation easier, enables some operations that are difficult in 'Vanilla' JS, and standardizes cross-browser compatibility. It's still very popular (and thus worth familiarizing yourself with), but it was more useful in the past. JavaScript got better, and front-end frameworks like Angular, React, and Vue emerged. You shouldn't build complex pages using jQuery because they quickly become unmanageable, but it's still very common and useful for simpler pages. You can learn more about jQuery [here](https://learn.jquery.com/) and [here](https://www.w3schools.com/jquery/default.asp). There's also [jQuery Mobile](http://jquerymobile.com/) and [jQuery UI](https://jqueryui.com/). There's also an [anti-jQuery blog](https://blog.garstasio.com/you-dont-need-jquery/).

You can include jQuery by adding a script tag to a cdn in the HTML head, you can find links [here](http://code.jquery.com/). The 'minified' code has newlines and spaces removed so it's smaller and faster to parse. The 'slim' version has some features (e.g. ajax and animations) removed so it's more lightweight.

## Wrappers

jQuery uses special 'wrappers' around elements in order to add additional functionality.

```html
<body>
  <div id="mydiv"></div>
</body>
```

```javascript
//element targeted in JS
const mydiv = (document.getElementById("mydiv").innerText = "hello world!");
//element targeted in jQuery
$("#mydiv").text("hello world!");
```

You can also create a variable using the \$ sign and assign a complext HTML element in a more easy way:

```html
<input type="text" value="" id="text-field" />
<button id="btn-list">click to Add to List</button>
<ul id="list">
  <li>snow</li>
  <li>sleet</li>
  <li>wind</li>
</ul>
<script>
  $("#btn-list").on("click", function () {
    const $li = "<li>" + $("#text-field").val() + "</li>";
    $("#list").append($li);
  });
</script>
```

## Executing On Page Load

jQuery uses a special `ready` event which occurs after the HTML of the page has been loaded, but before the content (images, etc) have been loaded. The `load` event is executed after the content has been loaded.

Without jQuery:

```javascript
window.onload = function () {
  console.log("loaded!");
};
```

With jQuery:

```javascript
$(document).ready(function () {
  console.log("ready!");
});
```

Or more succinctly:

```javascript
$(function () {
  console.log("ready!");
});
```

## Selecting Elements

One major advantage of jQuery is that it simplifies the selection of elements. Note that these return special jQuery objects, which are wrapped around the Vanilla JS objects. You can find more about selectors [here](http://api.jquery.com/category/selectors/).

- `$('#header')` select the element with an ID of 'header'
- `$('li')` select all li tags on the page
- `$('ul li')` select list items that are in unordered lists
- `$('.person')` select all elements with a class of 'person'

## Getting and Setting Values

### HTML

```javascript
$("#mydiv").html(); // get the innerHTML
$("#mydiv").html("<b>New HTML</b>"); // set the innerHTML

$("#mydiv").text(); // get the innerText
$("#mydiv").text("New Text"); // set the innerText

// add explanation points to the innerHTML of every li element
$("li").html(function (index, oldHtml) {
  return oldHtml + "!!!";
});

// iterate through each li element
$("li").each(function (index, elem) {
  // this: the current, raw DOM element
  // index: the current element's index in the selection
  // elem: the current, raw DOM element (same as this)
  $(this).prepend("<b>" + index + ": </b>");
});
```

### Attributes

```javascript
// set the disabled attribute on all inputs
$("input").attr("disabled", true);
$("input").attr("disabled", "disabled");

//remove it
$("input").removeAttr("disabled");
```

### CSS

```javascript
// add the css class 'red'
$("li").addClass("red");

// remove the css class 'red'
$("li").removeClass("red");

// set a css property
$("li").css({
  color: "red",
});

// hide an element
$("li").hide();
$("li").show();
```

## Chaining

```html
<button id="clickme">Click here</button>

<ul id="list">
  <li>snow</li>
  <li>sleet</li>
  <li>wind</li>
</ul>

<script>
  $("#clickme").click(function () {
    $("li")
      .css("background-color", "red")
      .slideDown()
      .fadeOut("slow")
      .fadeIn()
      .slideUp();
  });
</script>
```

## Creating and Appending Elements

```javascript
const div = $("<div>", { id: "foo", class: "a" }).css({
  "background-color": "red",
  width: "100px",
  height: "100px",
});
$("body").append(div);
```

## Events

```javascript
$("p").click(function () {
  // action goes here!!
});

$("p").dblclick(function () {
  $(this).hide();
});

$("#p1").mouseenter(function () {
  alert("You entered p1!");
});

$("#p1").mouseleave(function () {
  alert("You left p1!");
});

$("#p1").mousedown(function () {
  alert("Mouse down over p1!");
});

$("#p1").mouseup(function () {
  alert("Mouse up over p1!");
});

$("p").on({
  mouseenter: function () {
    $(this).css("background-color", "lightgray");
  },
  mouseleave: function () {
    $(this).css("background-color", "lightblue");
  },
  click: function () {
    $(this).css("background-color", "yellow");
  },
});
```

## Animation

```javascript
$("li").fadeIn();

$("li").animate({
  left: "+=100",
});
```

## This in jQuery

Whatever be the event/method ??? like click, hover, each, blur. You can refer to the DOM element with \$(this).

```html
<ul>
  <li>first</li>
  <li>second</li>
  <li>third</li>
  <li>forth</li>
</ul>

<script>
  $("li").click(function () {
    $(this).css("color", "orange");
  });
</script>
```

## AJAX

```javascript
$.ajax({
  url: "http://example.com",
}).done(function (data) {
  alert(data);
});
```
