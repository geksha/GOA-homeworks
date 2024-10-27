function Elements(arr1, arr2) {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);
    
    const common = [];
    
    for (const item of set2) {
        if (set1.has(item)) {
            common.push(item);
        }
    }
    
    return common;
}

const arr1 = [1, 2, 3, 4, 5];
const arr2 = [4, 5, 6, 7, 8];
console.log(commonElements(arr1, arr2));