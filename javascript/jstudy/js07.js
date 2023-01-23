'use strict';

// array declaration
const arr1 = new Array();
const arr2 = [1, 2];

// index position
const fruits = ['🍎', '🍌', '🍇'];
console.log(fruits);
console.log(fruits[0]);
console.log(fruits[2]);
console.log(fruits[3]);
console.log(fruits.length);

// looping
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

for (let fruit of fruits) {
  console.log(fruit);
}

fruits.forEach(function (fruit, index) {
  console.log(fruit, index);
});

fruits.forEach((fruit, index) => console.log(fruit, index));

// add, delete, copy
fruits.push('🍉', '🍋');
console.log(fruits);

fruits.pop();
console.log(fruits);

fruits.unshift('🍅', '🥝');
console.log(fruits);

fruits.shift();
console.log(fruits);

fruits.splice(2, 1);
console.log(fruits);

fruits.splice(1, 1, '🍏', '🍋');
console.log(fruits);

const fruits2 = ['🍏', '🍍', '🍑'];
const fruits3 = fruits.concat(fruits2);
console.log(fruits3);

// search
console.log(fruits.indexOf('🍋'));
console.log(fruits.indexOf('🍑'));
console.log(fruits.includes('🍎'));
console.log(fruits.includes('🍏'));

console.log(fruits3.indexOf('🍏'));
console.log(fruits3.lastIndexOf('🍏'));
