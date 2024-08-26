const p = document.getElementById("paragraph")
const button = document.getElementById("btn1")
const button = document.getElementById("btn2")

let number = 0

button.addEventListener("click",function(){
    number += 1
    p.textContent = number
})

button.addEventListener("click",function(){
    number -= 1
    p.textContent = number
})


