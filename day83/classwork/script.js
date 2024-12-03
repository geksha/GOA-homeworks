// Base class: Animal
class Animal {
    constructor(name, habitat, diet, imageUrl) {
        this.name = name;
        this.habitat = habitat;
        this.diet = diet;
        this.imageUrl = imageUrl;
    }

    get description() {
        return `${this.name} lives in ${this.habitat} and eats a ${this.diet} diet.`;
    }

    createCard() {
        const card = document.createElement('div');
        card.classList.add('animal-card');

        const image = document.createElement('img');
        image.classList.add('animal-image');
        image.src = this.imageUrl;
        image.alt = `${this.name} image`;

        const name = document.createElement('h2');
        name.textContent = this.name;

        const info = document.createElement('div');
        info.classList.add('animal-info');
        info.innerHTML = `
<p><strong>Habitat:</strong> ${this.habitat}</p>
<p><strong>Diet:</strong> ${this.diet}</p>`;

        card.appendChild(image);
        card.appendChild(name);
        card.appendChild(info);

        return card;
    }
}

// Subclass: Mammal
class Mammal extends Animal {
    constructor(name, habitat, diet, imageUrl, hasFur = true) {
        super(name, habitat, diet, imageUrl);
        this.hasFur = hasFur;
    }

    createCard() {
        const card = super.createCard();
        const furInfo = document.createElement('p');
        furInfo.innerHTML = `<strong>Has Fur:</strong> ${this.hasFur ? 'Yes' : 'No'}`;
        card.querySelector('.animal-info').appendChild(furInfo);
        return card;
    }
}

class Bird extends Animal {
    constructor(name, habitat, diet, imageUrl, canFly = true) {
        super(name, habitat, diet, imageUrl);
        this.canFly = canFly;
    }

    get flyingAbility() {
        return this.canFly ? `${this.name} can fly.` : `${this.name} cannot fly.`;
    }

    createCard() {
        const card = super.createCard();
        const flightInfo = document.createElement('p');
        flightInfo.innerHTML = `<strong>Can Fly:</strong> ${this.canFly ? 'Yes' : 'No'}`;
        card.querySelector('.animal-info').appendChild(flightInfo);
        return card;
    }
}

class AnimalWikiApp {
    constructor() {
        this.animals = {};
    }

    addAnimal(animal) {
        this.animal.push(animal);
    }

    renderAnimals() {
        const animalList = document.getElementById('animal-list');
        animalList.innerHTML = '';

        this.animals.forEach(animal => {
            console.log("kej")
            const card = animal.createCard();
            animalList.appendChild(card);
        });
    }
}

const app = new AnimalWikiApp();


app.addAnimal(new Mammal('Tiger', 'Forests', 'Carnivore', './images/tiger.jpg', true));
app.addAnimal(new Bird('Penguin', 'Antarctica', 'Carnivore', './images/penguin.jpg', true));
app.addAnimal(new Mammal('Panda', 'Forests', 'Herbivore', './images/panda.jpg', true));
app.addAnimal(AnimalWikiUtils.createRandomAnimal());

app.renderAnimals();