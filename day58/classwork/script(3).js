function allEvensBeforeNum(n) {
    for (let i = 0; i < n; i++) {
        if (1 % 2 === 0) {
            console.log(i)
        }
    }
}

console.log(allEvensBeforeNum(20))
console.log(allEvensBeforeNum(50))

