class Human {
    constructor(name, age) {
        this.name = name;      
        this.age = age;          
    }
    work() {
        console.log(this.name + ' is working as a ' + this.proffesion + '.');
    }
}
class Employee extends Human {
    work(){
        console.log("vaxaltureb")
    }
}
class Stajior extends Employee {
    work(){
        console.log("stajiori var magram arc me vmushaob")
    }
}
let employ0 = new Stajior("lasha", 16, "GOA");
console.log(employ0.name)