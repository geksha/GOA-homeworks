class Animal {
    constructor(name, age){
        this.name = name;
        this.age = age;
        this.group = group;
    }
}

class Mammal extends Animal {
    constructor(name, age){
        super.(name,age);
        this.gorup = group;
    }
}

class Dog extends Animal {
    constructor(name, age){
        super(name,age);
        this.group = group;
    }
}

let mammal1 = new Mammal("aqlemi", "4", "xerxemliani")
let dog1 = new Dog("avchalka", "2", "xerxemliani")
console.log(mammal1.name)
console.log(dog1.name)