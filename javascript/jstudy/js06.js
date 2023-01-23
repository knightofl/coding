'use strict';

const name = 'knight';
const age = 4;
print(name, age);
function print(name, age) {
  console.log(name);
  console.log(age);
}

const knightofl = { name: 'knight', age: 21 };
oPrint(knightofl);
function oPrint(man) {
  console.log(man.name);
  console.log(man.age);
}
console.log(knightofl['name']);
knightofl.job = 'doctor';
console.log(knightofl.job);
delete knightofl.job;
console.log(knightofl.job);
knightofl['job'] = 'fighter';
console.log(knightofl.job);

// object = { key: value };
const obj1 = {}; // object literal syntax
const obj2 = new Object(); // object constructor syntax

function printValue(obj, key) {
  console.log(obj[key]);
  //console.log(obk.key);
}
printValue(knightofl, 'name');
printValue(knightofl, 'age');

// property value shorthand
function makePerson1(name, age) {
  return {
    name: name,
    age: age,
  };
}
function makePerson2(name, age) {
  return {
    name,
    age,
  };
}
const person1 = makePerson1('lp3s', 22);
const person2 = makePerson2('knight', 21);
console.log(person1);
console.log(person2);

// constructor function
function Person(name, age) {
  // this = {};
  this.name = name;
  this.age = age;
  // return this;
}
const person3 = new Person('kitty', 23);
console.log(person3);

// in operator
console.log('name' in person3);
console.log('job' in person3);

for (let key in knightofl) {
  console.log(key);
}

const array = [1, 2, 3, 4, 5];
for (let i = 0; i < array.length; i++) {
  console.log(array[i]);
}
for (let val of array) {
  console.log(val);
}

// cloning
const person4 = person3;
person4.name = 'cat';
console.log(person3.name);

// copy old way
const person5 = {};
for (let key in person3) {
  person5[key] = person3[key];
}

const person6 = {};
Object.assign(person6, person3);

const person7 = Object.assign({}, person3);

console.log(person5);
console.log(person6);
console.log(person7);

const fruit1 = { color: 'red' };
const fruit2 = { color: 'blue', size: 'big' };
const fruit3 = { size: 'mid' };
const mixed = Object.assign({}, fruit1, fruit2, fruit3);
console.log(mixed.color);
console.log(mixed.size);
