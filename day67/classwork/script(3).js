const p = document.getElementById("count");
const btn = document.getElementById("incremenet");

let count = 0;

function counter() {
    count++;
    p.textContent = count;

    if(count >= 10){
        btn.removeEventListener('click', counter);
    } 
}

btn.addEventListener('click', counter)