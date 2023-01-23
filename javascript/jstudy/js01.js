'use strict';

let a = 4;
console.log(a);

a = 5;
console.log(a);

let name = 'lupin3se';
console.log(name);

name = 'knightofl';
console.log(name);

const b = 4;
console.log(b);
// b = 5;

console.log(`a value: ${a}, type: ${typeof a}`);
console.log(`b value: ${b}, type: ${typeof b}`);
console.log(`name value: ${name}, type: ${typeof name}`);

const infinity = 1 / 0;
const negativeInfinity = -1 / 0;
const nAn = 'string' / 2;
console.log(infinity);
console.log(negativeInfinity);
console.log(nAn);

const bigInt = 12345n;
console.log(`bigInt value: ${bigInt}, type: ${typeof bigInt}`);

const canRead = true;
const test = 3 < 1;
console.log(`canRead value: ${canRead}, type: ${typeof canRead}`);
console.log(`test value: ${test}, type: ${typeof test}`);

let nothing = null;
let x;
console.log(`nothing value: ${nothing}, type: ${typeof nothing}`);
console.log(`x value: ${x}, type: ${typeof x}`);

const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(`symbol1 value: ${symbol1.description}, type: ${typeof symbol1}`);
console.log(`symbol2 value: ${symbol2.description}, type: ${typeof symbol2}`);
console.log(symbol1 === symbol2);

const gSymbol1 = Symbol.for('id');
const gSymbol2 = Symbol.for('id');
console.log(
  `gSymbol1 value: ${gSymbol1.description}, type: ${typeof gSymbol1}`
);
console.log(
  `gSymbol2 value: ${gSymbol2.description}, type: ${typeof gSymbol2}`
);
console.log(gSymbol1 === gSymbol2);

const knightofl = { name: 'lee', age: 50 };
console.log(`knightofl value: ${knightofl}, type: ${typeof knightofl}`);
knightofl.age = 21;

let text = 'hello';
console.log(text.charAt(0));
console.log(`text value: ${text}, type: ${typeof text}`);
text = 1;
// console.log(text.charAt(0))
console.log(`text value: ${text}, type: ${typeof text}`);
text = '2' + 4;
console.log(`text value: ${text}, type: ${typeof text}`);
text = '8' / 2;
console.log(`text value: ${text}, type: ${typeof text}`);
