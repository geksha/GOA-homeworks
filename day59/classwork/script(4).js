const messageBox = document.getElementById("message")
const countBox = document.getElementById("count")

messageBox.addEventListener("input",counter)

function counter(){
    const limit = 200;
    let currect_count = countBox.value.length

    if(currect_count > limit){
        countBox.textContent = "Character limit exceeded"
    }
    else{
        countBox.textContent = "green"
        countBox.textContent = current_count + "/" + limit;
    }
}