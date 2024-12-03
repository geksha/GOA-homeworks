function Elements(arr1, arr2) {

    const set1 = new Set(arr1);
    const set2 = new Set(arr2);
    
    const commonElements = [...set1].filter(item => set2.has(item));
    
    return commonElements;
}

const arr1 = [1, 2, 3, 4, 5];
const arr2 = [4, 5, 6, 7, 8];
const result = Elements(arr1, arr2);
console.log(result); 