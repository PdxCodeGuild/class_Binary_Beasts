# Objects

Objects are the foundation of JavaScript and permeate its every aspect. Almost everything in JavaScript is an object. In fact, only six things are not objects. They are — *null,undefined, strings, numbers, boolean, and symbols.* These are called primitive values or primitive types.
Anything that is not a primitive value is an Object.

Objects look like Python Dictionaries, but have attributes (variable names) instead of keys (strings).

An object like this below is referred to as an object literal. This is in contrast to objects instantiated from classes, which we'll look at later on.

```javascript
const library_user = {
    first_name: 'Jane',
    last_name: 'Smith',
    age: 20,
    books: [{
        title: 'A Wrinkle in Time',
        author: 'Madeleine L\'Engle',
        published: 1962
    },{
        title: 'The Giving Tree',
        author: 'Shel Silverstein',
        published: 1964
    }],
    printFullName() {
    return `${this.first_name} ${this.last_name}`
  }
   greeting: function() {
    alert('Hi! I\'m ' + this.first_name + '.');
  }:
};
};
console.log(library_user.first_name); // Jane
console.log(library_user.books[0].title); // A Wrinkle in Time
console.log(library_user.printFullName)
console.log(library_user.greeting())
```

You can also access the attributes of an object as you would a dictionary.

```javascript
console.log(library_user["first_name"]);
// Jane
console.log(library_user.books[0]["title"]);
// A Wrinkle in Time
```
## You've been using objects all along

So when you used string methods like:

```Javascript

myString.split(',');

```

You were using a method available on an instance of the String class. Every time you create a string in your code, that string is automatically created as an instance of String, and therefore has several common methods and properties available on it.