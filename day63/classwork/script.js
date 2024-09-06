function manualFilter(a, Array) {
    let result = [];
    for (let i = 0; i < Array.length; i++) {
        let element = Array[i];

        if (a(element)) {

            result.push(element);
        }
    }

    return result;
}

function isEven(number) {
    return number % 2 === 0;
}

let numbers = [1, 2, 3, 4, 5, 6];
let evenNumbers = manualFilter(isEven, numbers);

console.log(evenNumbers);

