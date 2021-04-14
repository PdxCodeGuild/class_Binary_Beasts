# Prototypes

JavsScript isn't a class based language. Classes are syntactic sugar built on top of prototypes. JavaScript is often described as a prototype-based language.

- Prerequisite:
  [Objects in Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)

- Resources:
  Read more [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain) and [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)

Do you remember when we learned that in Python everything is an object? If you run the following command in Python, you'll see all the methods associated with the instance of the integer object.

```Python
x = 5
print(dir(x))
```

Javascript uses prototypes, which are the mechanism by which objects inherit features from one another. A prototype is a collection of methods that are are being used by any object type.

Any object in Javascript has a prototype: arrays, date, integers, custom classes, etc.

Let's take a look at the following example:

```Javascript
const arr = [1,2,3]
console.log(arr)
```

If you open your browser window, look for `__proto__` in the JavaScript console. You'll see that it includes methods coming from the Array object. You can find all methods that JavaScript attached to the Array prototype with `Array.prototype or arr.__proto__`

```Javascript
arr.__proto__ === Array.prototype;
arr.__proto__.__proto__ === Object.prototype;
```

We can also use the isPrototypeOf() method to accomplish this.

```Javascript
Array.prototype.isPrototypeOf(arr);
Object.prototype.isPrototypeOf(Array);

arr instanceof Array;
```

let's try this:

```Javascript
function fun(){
}
```

If you start typing `fun.` you'll see methods available to this function. But where these methods are coming from?

Last example:

```Javascript
const obj = {
  name: 'alex',
  lastName: 'D'
}
console.log(obj)
```

You'll see again methods available in the **proto** object. These methods are coming from the Object object.

Every array, object, function, has a prototype, or a blueprint from which these types inherit methods. Try this in the console:

```
Array.prototype
Function.prototype
Object.prototype
Set.prototype
Boolean.prototype
```

You can modify add each blueprint's methods. For instance, you could add the following property to the Array prototype:

```Javascript
Array.prototype.hello = function(){alert('hello')}
```

Then try the following:

```Javascript
const myList = [1]
Object.getPrototypeOf(myList); //
myList.hello()
```

This means that every instance of the Array prototype can use this method. You have just discovered the prototype chain! Properties and methods of instances are found by walking up the chain of prototypes.

You can also delete the `.concat()` method from the Array prototype! You can try this:

```Javascript
delete Array.prototype.concat
```

## Constructor Functions

Constructor functions are functions that are used to construct new objects. This syntax here allows functions to create objects `(){}`

```Javascript
function Car(color, model, year){  //capitalized for convention, so we use the keyword 'new'
  this.color = color,
  this.model = model,
  this.age = year
  this.run = function(){
    console.log('going fast!')
  }
}


const ford = new Car('red', 'sport', '1945')
const fiat = new Car('red', 'convertible', '1960')

console.log(ford,fiat)
// Car {color: "red", model: "sport", age: "1945", run: ƒ}
// Car {color: "red", model: "convertible", age: "1960", run: ƒ}
```

We notice above that all instances of Car bear the method 'run', which is a memory waste and is redundant. To optimize this, we can add this method to the Car prototype and walk up the chain.

```Javascript

Car.prototype.run = function(){
  console.log('going fast!')
}
Car.prototype.me = function(){
  return this
}

console.log(ford.run()) //going fast!
console.log(ford.me()) //Car {color: "red", model: "sport", age: "1945"}
console.log(fiat.run()) //going fast!
console.log(fiat.me()) //Car {color: "red", model: "convertible", age: "1960"}
```

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
//Dog.prototype = new Animal; ??

Dog.prototype.bark = function () {
  console.log(this.sound);
};

const myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk'
myDog.bark(); // logs 'ruff'
```

## Syntactic sugar : Classes

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
