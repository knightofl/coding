'use strict';

// Object to JSON
let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple', 'banana']);
console.log(json);

const rabbit = {
  name: 'tori',
  color: 'white',
  size: null,
  birthDate: new Date(),
  jump: () => {
    console.log(`${name} can jump!`);
  },
};
json = JSON.stringify(rabbit);
console.log(json);

json = JSON.stringify(rabbit, ['name', 'color']);
console.log(json);

json = JSON.stringify(rabbit, (key, value) => {
  console.log(`key: ${key}, value: ${value}`);
  return key === 'name' ? 'knightofl' : value;
});
console.log(json);

// JSON to Object
json = JSON.stringify(rabbit);
const obj = JSON.parse(json, (key, value) => {
  return key === 'birthDate' ? new Date(value) : value;
});
console.log(obj);

//rabbit.jump();
//obj.jump();

console.log(rabbit.birthDate.getDate());
console.log(obj.birthDate.getDate());

// JSON Diff checker: http://www.jsondiff.com/
// JSON Beautifier/editor: https://jsonbeautifier.org/
// JSON Parser: https://jsonparser.org/
// JSON Validator: https://tools.learningcontainer.com/json-validator/
