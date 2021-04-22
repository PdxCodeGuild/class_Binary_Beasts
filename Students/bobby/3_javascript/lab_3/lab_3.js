// Version #1

// const ranSites =["http://www.mozilla.org", "http://www.google.com", "http://www.youtube.com"]

// function pickSites() {
//     let randomSites = Math.round(Math.random() * 2);
//     return ranSites[randomSites]
// }

// const redirect = document.getElementById("btn")

// redirect.addEventListener("click", function() {
//     const site = pickSites()
//     window.open(site)
// })


//--------------------------------------------------------------------

// Version #2

// const ranSites =["http://www.mozilla.org", "http://www.google.com", "http://www.youtube.com"]

// function pickSites() {
//     let randomSites = Math.round(Math.random() * 2);
//     return ranSites[randomSites]
// }

// const redirect = document.getElementById("btn")

// redirect.addEventListener("click", function() {
//     function timer() {
//         setTimeout(myTimer1, 0)
//         setTimeout(myTimer2, 1000)
//         setTimeout(myTimer3, 2000)
//     }
//     function myTimer1() {
//         document.getElementById("timer").innerHTML = "3 seconds";
//         console.log("3")
//     }
//     function myTimer2() {
//         document.getElementById("timer").innerHTML = "2 seconds";
//         console.log("2")
//     }
//     function myTimer3() {
//         document.getElementById("timer").innerHTML = "1 seconds";
//         console.log("1")
//     }
//     function openSite() {
//         const site = pickSites()
//         window.open(site)
//     }
//     setTimeout(openSite, 3000)
//     timer()   
// })

// setInterval

// console.log(setInterval)