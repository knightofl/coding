'use strict';

console.log('my' + 'Cat');
console.log('2' + 4);
console.log(`${1 + 2}`);
console.log("knight's armor");

console.log(1 + 1);
console.log(4 - 2);
console.log(4 / 2);
console.log(2 * 4);
console.log(5 % 2);
console.log(2 ** 4);

let a = 3;
console.log(++a);
console.log(a++);
console.log(a);

const val1 = true;
const val2 = 4 < 2;
console.log(val1 || val2);
console.log(val1 && val2);
console.log(!val2);

const stringFive = '5';
const numberFive = 5;
console.log(stringFive == numberFive);
console.log(stringFive != numberFive);
console.log(stringFive === numberFive);
console.log(stringFive !== numberFive);

const knight1 = { name: 'knightofl' };
const knight2 = { name: 'knightofl' };
const knight3 = knight1;
console.log(knight1 == knight2);
console.log(knight1 === knight2);
console.log(knight1 == knight3);
console.log(knight1 === knight3);

console.log(0 == false);
console.log(0 === false);
console.log('' == false);
console.log('' === false);
console.log(null == undefined);
console.log(null === undefined);

const name = 'knightofl';
if (name === 'knightofl') {
  console.log('Welcome, knightofl!');
} else if (name === 'coder') {
  console.log('Hi, coder!');
} else {
  console.log('Unknown!');
}

console.log(name === 'lupin3se' ? 'yes' : 'no');

const browser = 'firefox';
switch (browser) {
  case 'edge':
    console.log('Welcome Edge');
    break;
  case 'chrome':
    console.log('Evil Google');
    break;
  case 'firefox':
    console.log('Cheer Up');
    break;
  default:
    console.log('How are you');
    break;
}

let i = 3;
while (i > 0) {
  console.log(`while: ${i}`);
  i--;
}

i = 3;
do {
  console.log(`do while: ${i}`);
  i--;
} while (i > 0);

for (let i = 3; i > 0; i--) {
  console.log(`for: ${i}`);
}

for (let i = 0; i <= 10; i++) {
  if (i % 2 === 0) {
    continue;
  }
  console.log(i);
}

for (let i = 1; i <= 10; i++) {
  for (let j = 1; j <= 10; j++) {
    if ((i * j) % 7 === 0) {
      console.log(`i: ${i}, j: ${j}`);
    }
  }
}
