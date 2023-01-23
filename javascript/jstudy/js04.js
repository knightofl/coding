'use strict';

function calculate(command, a, b) {
  switch (command) {
    case '+':
      return a + b;
    case '-':
      return a - b;
    case '*':
      return a * b;
    case '/':
      return a / b;
    default:
      throw Error('not command');
  }
}

console.log(calculate('+', 8, 2));
console.log(calculate('-', 8, 2));
console.log(calculate('*', 8, 2));
console.log(calculate('/', 8, 2));
