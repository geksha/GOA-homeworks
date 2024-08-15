const p = document.getElementById("paragraph")
const button = document.getElementById("btn")

// console.log(p.textContent)

// let number = 5

// console.log(number + 10)

p.textContent = "Hello world"

let number = 0 

button.addEventListener("submit",function(){
    number += 1
    p.textContent = number
})
