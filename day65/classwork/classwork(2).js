const myP = document.getElementsByClassName('family');

console.log(pArr)

function manualGetElementsByClassName(className) {
    const elements = document.all;
    const result = [];

    for(let i = 0; i < elements.length; i++) {
        if(elements[i].classList.contains(className)) {
            result.push(elements[i]);
        }
    }

    return result;
}