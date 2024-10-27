class Book {
    constructor(title, author, pages, genre) {
        this.title = title;
        this.author = author;
        this.pages = pages;
        this.genre = genre;
        this.read = false;
    }

    readBook() {
        this.read = true;
        console.log(`You have read "${this.title}" by ${this.author}.`);
    }

    info() {
        return `${this.title} by ${this.author}, ${this.pages} pages, Genre: ${this.genre}. ${this.read ? 'You have read this book' : 'You have not read this book'}`;
    }

    Describe() {
        console.log('name: ' + this.title);
        console.log('author: ' + this.species);
        console.log('pages: ' + this.pages);
        console.log('genre: ' + this.genre )
    }
}

const myBook = new Book('1984', 'George Orwell', 328, 'Dystopian');
console.log(myBook.info());
myBook.readBook();
console.log(myBook.Describe());


