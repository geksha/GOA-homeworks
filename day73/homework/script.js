class Human {
    constructor(name, age, gender, profession) {
        this.name = name;      
        this.age = age;          
        this.gender = gender;    
        this.profession = profession;  
    }
    greet() {
        console.log('Hello, my name is ' + this.name + '.');
    }
    introduce() {
        console.log('I am ' + this.name + ', ' + this.age + ' years old, and I work as a ' + this.profession + '.');
        console.log(`I am ${this.name}, ${this.age} years old, and I work as a ${this.profession}.`);
    }
    work() {
        console.log(this.name + ' is working as a ' + this.profession + '.');
    }
    displayDetails() {
        console.log('Name: ' + this.name);
        console.log('Age: ' + this.age);
        console.log('Gender: ' + this.gender);
        console.log('Profession: ' + this.profession);
    }
    static generalInfo() {
        console.log('Humans are highly intelligent beings');
    }
}

class Employee extends Human {
    constructor(name, age, gender, profession, companyName) {
        super(name, age, gender, profession);
        this.companyName = companyName;
    }
    introduce() {
        super.introduce();
        console.log('I work at ' + this.companyName + '.');
    }
    work() {
        console.log(this.name + ' is working as a ' + this.profession + ' at ' + this.companyName + '.');
    }
    static employeeInfo() {
        console.log('Employees are people who work for an company.');
    }
}


let person1 = new Human('Irodi', 25, 'male', 'web developer');
let employee1 = new Employee('Jane', 30, 'female', 'software engineer', 'TechCorp');


person1.greet();
person1.introduce();
person1.work();
person1.displayDetails();
Human.generalInfo();  



employee1.greet();
employee1.introduce();
employee1.work();
employee1.displayDetails();
Employee.employeeInfo();