cinst password = "luka1234";
let pass;
let attemps = 3;

while(attemps > 0 && password !== pass){
    let pass = prompt("Emter your password");
    if(pass !== password){
        attempts --
        alert("You have " + attempts + "left")
    }
    else {
        alert("Access granted")
        break;
    }
    if(attempts === 0){
        alert("System blocked, you have run out of tries")
    }
}