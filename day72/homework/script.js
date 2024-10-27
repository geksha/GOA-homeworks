class Animal {
    constructor(name, species, age) {
        this.name = name;
        this.species = species;
        this.age = age;
    }
    speak() {
        console.log(this.name + " make a sound.");
    }
    displayDetails() {
        console.log('Name ' + this.name);
        console.log('Species: ' + this.species);
        console.log('Age: ' + this.age + ' years');
    }
}
let lion = new Animal('alika', 'Lion', 5);
lion.speak()
lion.displayDetails();