const pArr = document.getElementsByTagName('p');

console.log(pArr)



function manualGetElementsByTagName(tagName) {
    const elements = document.all;
    const result = [];

    for(let i = 0; i < elements.length; i++) {
        if(elements[i].tagName === tagName.toUpperCase()) {
            result.push(elements[i]);
        }
    }

    return result;
}


console.log(manualGetElementsByTagName('p'))