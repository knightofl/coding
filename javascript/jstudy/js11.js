'use strict';

// Promise is a Javascript Object for asynchronous operation
// state: pending => fulfilled or rejected
// Producer vs Consumer

// Producer
// When new Promise is created, the executor runs automatically.
const promise = new Promise((resolve, reject) => {
  console.log('doing something...');
  setTimeout(() => {
    //resolve('knightofl');
    reject(new Error('no network'));
  }, 2000);
});

// Consumer: then, catch, finally
promise
  .then((value) => {
    console.log(value);
  })
  .catch((error) => {
    console.log(error);
  })
  .finally(() => {
    console.log('finally executed');
  });

// promise chaining
const fetchNumber = new Promise((resolve, reject) => {
  setTimeout(() => resolve(1), 1000);
});

fetchNumber
  .then((num) => num * 2)
  .then((num) => num * 3)
  .then((num) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(num - 1), 1000);
    });
  })
  .then((num) => console.log(num));

// Error Handling
const getHen = () =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve('🐓'), 1000);
  });

const getEgg = (hen) =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve(`${hen} => 🥚`), 1000);
    //setTimeout(() => reject(new Error(`error! ${hen} => 🥚`)), 1000);
  });

const cook = (egg) =>
  new Promise((resolve, reject) => {
    setTimeout(() => resolve(`${egg} => 🍳`), 1000);
  });

getHen()
  .then((hen) => getEgg(hen))
  .then((egg) => cook(egg))
  .then((fry) => console.log(fry));

getHen() //
  .then(getEgg)
  .catch((error) => {
    return '🥪';
  })
  .then(cook)
  .then(console.log)
  .catch(console.log);
