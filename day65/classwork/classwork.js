console.dir(document.getElementById('me'));

function manualGetElementById(id) {
    const elements = documents.all;

    for(let i = 0; i < elements/length; i++) {
        if(elements[i].id === id) {
            return elements[i];
        }
    }
}

console.log(manualGetElementById('me'));