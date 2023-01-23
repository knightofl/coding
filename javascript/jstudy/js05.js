'use strict';

class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  speak() {
    console.log(`${this.name} is ${this.age} years old.`);
  }
}

const person = new Person('Lee', 21);
person.speak();

person.name = 'Kim';
person.age = 50;
person.speak();

class User {
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }

  get age() {
    return this._age;
  }

  set age(value) {
    if (value < 0) {
      throw Error('age cannot be negative.');
    }
    this._age = value;
  }
}

const user1 = new User('Steve', 'Jobs', 21);
console.log(user1.age);

// const user2 = new User('Steve', 'Wozniak', -1);

class Experiment {
  publicField = 2;
  #privateField = 3;
}
const experiment = new Experiment();
console.log(experiment.publicField);
console.log(experiment.privateField);

class Article {
  static publisher = 'knight of l';
  constructor(articleNumber) {
    this.articleNumber = articleNumber;
  }
  static printPublisher() {
    console.log(Article.publisher);
  }
}
const article = new Article(1);
console.log(article.publisher);
console.log(Article.publisher);
//article.printPublisher();
Article.printPublisher();

class Shape {
  constructor(width, height, color) {
    this.width = width;
    this.height = height;
    this.color = color;
  }

  draw() {
    console.log(`drawing ${this.color} color`);
  }

  getArea() {
    return this.width * this.height;
  }
}

class Rectangle extends Shape {}
const rectangle = new Rectangle(10, 20, 'blue');
rectangle.draw();
console.log(rectangle.getArea());

class Triangle extends Shape {
  getArea() {
    return (this.width * this.height) / 2;
  }
}
const triangle = new Triangle(10, 20, 'red');
triangle.draw();
console.log(triangle.getArea());

console.log(rectangle instanceof Rectangle);
console.log(rectangle instanceof Shape);
console.log(triangle instanceof Triangle);
console.log(triangle instanceof Shape);
console.log(rectangle instanceof Triangle);
console.log(triangle instanceof Object);
console.log(triangle.toString());
