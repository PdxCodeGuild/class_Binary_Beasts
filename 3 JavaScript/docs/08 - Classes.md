# add Prototypes here

Do you remember when we learned that in Python everything is an object? If you run the following command in Python, you'll see all the methods associated with the list object.

```Python
print(dir([]))
```

Javascript uses prototypes, which are the mechanism by which objects inherit features from one another. A prototype is a collection of methods that are are being used by any object type.

Any object in Javascript has a prototype: arrays, sets, integers, custom classes, etc.

```Javascript
const arr = [1,2,3]
console.log(arr)
```

If you open your browser window, look for `__proto__` in the JavaScript console.

## Classes, introductory Example

ES6 introduced a much easier way of writing classes. Below is an example comparing the use of a class to that of an object. The object behaves similarly, except you'll have to re-write the entire structure every time you create an instance. Also, each instance will have its own copy of the `getBalance` function, resulting in greater memory overhead.

```javascript
// using a class
class Atm {
  constructor(balance = 0) {
    this.balance = balance;
  }
  getBalance() {
    return this.balance;
  }
}

const wellsFargo = new Atm();
const chase = new Atm();
console.log(wellsFargo.getBalance());

// using an object
const atm = {
  balance: 5.0,
  getBalance: function () {
    return this.balance;
  },
};

console.log(atm.getBalance());
```

## Inheritance

```javascript
class Animal {
  constructor(legs = 0) {
    this.legs = legs;
  }

  move() {
    if (this.legs > 0) {
      console.log("walk");
    } else {
      console.log("slither");
    }
  }
}

class Dog extends Animal {
  constructor(legs = 4, sound = "ruff") {
    super(legs); // invoke the parent class's constructor
    this.sound = sound;
  }

  bark() {
    console.log(this.sound);
  }

  move() {
    // override the parent method
    super.move(); // call the parent method (optional)
    console.log("dog moving");
  }
}

const myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk', 'dog moving'
myDog.bark(); // logs 'ruff'
```

The way to do classes is ES5 is much more awkward, but you may see it in the wild, so it's worth knowing.

```javascript
function Animal(legs) {
  this.legs = legs || 0; // use default value if needed
}

Animal.prototype.move = function () {
  if (this.legs > 0) {
    console.log("walk");
  } else {
    console.log("slither");
  }
};

function Dog(legs, sound) {
  Animal.call(this, legs); // parent 'constructor'
  this.sound = sound || "ruff";
}

Dog.prototype = Object.create(Animal.prototype);

Dog.prototype.bark = function () {
  console.log(this.sound);
};

const myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk'
myDog.bark(); // logs 'ruff'
```

## Syntactic sugar

Functions and classes are objects. Functions inherit from the Object prototype and they can be assigned key: value pairs. These pairs are referred to as _properties_ and can themselves be functions (i.e., _methods_).

The most important thing to remember is that classes are just normal JavaScript functions and could be completely replicated without using the class syntax. It is special syntactic sugar added in ES6 to make it easier to declare and inherit complex objects. Let's see an example:

```javascript
function createNewPerson(name) {
  const obj = {};
  obj.name = name;
  obj.greeting = function () {
    console.log("Hi! I'm " + obj.name + ".");
  };
  return obj;
}
const john = createNewPerson("John");
john.name;
john.greeting();
```

To simplify, the same can be written as the following:

```javascript
function Person(name) {
  this.name = name;
  this.greeting = function () {
    console.log("Hi! I'm " + this.name + ".");
  };
}

const person1 = new Person("Bob");
console.log(person1.greeting());
```

Which becomes:

```javascript
class Person {
  constructor(name) {
    this.name = name;
  }
  greeting() {
    return this.name;
  }
}

const person1 = new Person("Bob");
console.log(person1.greeting());
```

Here's how inheritance looks like using functions:

```javascript
function Brick() {
  this.width = 10;
  this.height = 20;
}

function BlueGlassBrick() {
  Brick.call(this);

  this.opacity = 0.5;
  this.color = "blue";
}

let shape = new BlueGlassBrick();

console.log(shape.width);
```
