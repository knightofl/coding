'use strict';

function printHello() {
  console.log('Hello!');
}
printHello();

function log(message) {
  console.log(message);
}
log('Hi!');
log(1234);

function changeName(obj) {
  obj.name = 'coder';
}

const knightofl = { name: 'programmer' };
changeName(knightofl);
console.log(knightofl);

function showMessage(message, from) {
  console.log(`${message} by ${from}`);
}
showMessage('Hi!');

function showMessage2(message, from) {
  console.log(`${message} by ${(from = 'unknown')}`);
}
showMessage2('Hi!');

function printAll1(...args) {
  for (let i = 0; i < args.length; i++) {
    console.log(args[i]);
  }
}
printAll1('dreams', 'come', 'true');

function printAll2(...args) {
  for (const arg of args) {
    console.log(arg);
  }
}
printAll2('dreams', 'come', 'true');

let names = ['Paul McCartney', 'John Lennon', 'George Harrison', 'Ringo Starr'];

function printNames(item) {
  console.log(item);
}
names.forEach(printNames);

names.forEach(function (item) {
  console.log(item);
});

names.forEach((item) => {
  console.log(item);
});

names.forEach((item, index) => {
  console.log(index, item);
});

let data1 = names.map((item) => {
  return item;
});
console.log(data1);

let data2 = names.filter((item) => {
  return item.length < 12;
});
console.log(data2);

let data3 = names.some((item) => {
  return item.startsWith('J');
});
console.log(data3);

let data4 = names.every((item) => {
  return item.startsWith('J');
});
console.log(data4);

let data5 = names.find((item) => {
  // 처음에 찾은 거 하나만 반환
  return item.startsWith('J');
});
console.log(data5);

let data6 = names.findIndex((item) => {
  return item.startsWith('J');
});
console.log(data6);

let globalMessage = 'global';
function printMessage() {
  let message = 'hello';
  console.log(message);
  console.log(globalMessage);
}
printMessage();
//console.log(message);

function sum(a, b) {
  return a + b;
}
console.log(sum(1, 2));

const print = function () {
  console.log('function print');
};
print();

const printAgain = print;
printAgain();

const sumAgain = sum;
console.log(sumAgain(3, 5));

function randomQuiz(answer, printYes, printNo) {
  if (answer === 'love you') {
    printYes();
  } else {
    printNo();
  }
}
const printYes = function () {
  console.log('Yes!');
};
const printNo = function print() {
  console.log('No!');
};

randomQuiz('wrong', printYes, printNo);
randomQuiz('love you', printYes, printNo);

const simplePrint1 = function () {
  console.log('simple print!');
};
simplePrint1();

const simplePrint2 = () => console.log('simple print!');
simplePrint2();

const add = (a, b) => a + b;
console.log(add(4, 5));

(function hello() {
  console.log('IIFE');
})();
