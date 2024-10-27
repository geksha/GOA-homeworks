class Animal {
    constructor(name, age){
        this.name = name
        this.age = age
    }
    capabilities(){
        console.log("this animal moves");
        console.log("this animal breathes");
        console.log("this animal eats");
        console.log("this animal blinks");
    }
}

class Fish extends Animal {
    capabilities(){
        super.capabilities();
        console.log("this animal swims");
        console.log("this animal has fins");
    }
}
class Fish extends Animal {
    capabilities(){
        super.capabilities();
        console.log("")
    }
}

let fish1 = new Fish("bob", 2)
fish1.capabilities(); 