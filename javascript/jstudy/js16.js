'use strict';

function greet() {
  console.log(this.msg);
}
const obj = { msg: "Hello" };

greet.call(obj);   // "Hello"
greet.apply(obj);  // "Hello"
const bound = greet.bind(obj);
bound(); 