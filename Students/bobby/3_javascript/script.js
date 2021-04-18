// Primitive values
// String, Number, Boolean, Null, Undefined

let letter = "r"
console.log(letter.toLocaleUpperCase()) // Returns upper case

// Objects
const house = {
    city : "Portland",
    state : "Oregon"
}
console.log(house["city"])

for (let key in house){
    console.log(house[key], key) // for loop
}




const a = 5
const fruits = ["apple", "rear"] // this is an array
//.push adds to an array

const person = {
    age = "5",
    name = "david"
}
// this is a comment

/* comment */

const name = prompt("enter your name") // this is an input

console.log() // print
alert() // 

let a = 1
const s = "hello world"
console.log(`i'd like to say ${s}`)

// use === to compare
// !== not equal
// 
const temperature = 55
if (temperature < 60) {
    console.log("cold")
}
    else if (temperature < 80) {

}
// this is a function
function min(a,b) {
    return (a<b) ? a : b
}
console.log(min(5,4))

// obljects "Everything is an object" Like a library in python
const person = {
    first_name : "alex",
    last_name : "d",
    printFullName(){
        return `${this.first_name}`
    }
}
console.log(person)
console.log(person(printFullName))
console.log(person.last_name)

// (`hello my name is ${x}`) use the back ticks like an f string and $ sign to access variable

// .push adds to the end of the array

// loops

// while

let i = 0

While (i < 10) {
    console.log(i)
    i++
}

// for
const fruits = ["pear", "apple", "bananna"]
for (let i = 0 ; i<fruits.length; i++){
    console.log(fruits(key))
}
// || this is or
// && this is and


// Functions
function add(a, b){
    return a + b
}
console.log(add)

const video = {
    title : "titanic",
    name: function(){
        console.log(this) // this by itself will return entire object, this.something will call that key
    }
}
video.name()

//----------------------------------------------------------------------------------------------------

// DOM

const myDiv = document.getElementById("myDiv")

const allDivs = document.getElementsByTagName("div")
console.log(allDivs)

const byName = document.getElementsByName("adiv")
console.log(byName)

const withQuerySelector = document.querySelector("#mydiv")
console.log(withQuerySelector)

const withQuerySelectorAll = document.querySelectorAll(".myclass")
console.log(withQuerySelector)

div1.innerText = "hello world" // this adds to div1

div2.innerHTML = `<p><b>Hello World!<b><p>` // this adds to div1

// these change style
myDiv.style.fontSize = "24px"
myDiv.style.color = "red"
myDiv.style.border = "1px solid black"
myDiv.style.backgroundColor = "green"

// Setting Attributes
const example1 = document.getElementsByTagNameNS("h1") [0]
example1.setAttribute("class", "myColor")
console.log(example1)

// Input Fields
const text_field = document.getElementsById("user_input")

trigger.addEventListener("click", function(){
    console.log(text_field.value)
    output.innerHTML = text_field.value // outputs to the html
})

const btn = document.createElement("button") // created button
btn.style // style the button
const container = document.getElementsById("") // Target the element
container.appendChild(btn) // Append the element

constul = documet.getElementsByTagName("ul") [0]
for (let i = 0; i < ul.length; i++){ // for loop through ul (this needs fixed "It's in the notes")
    console.log(ul[i]) // you can use .children
}
// Select the elements
// varify the elemnts with console.log


// set the attribute
// get the element
// has attribute


