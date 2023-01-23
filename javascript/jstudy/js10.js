'use strict';

console.log('1');
setTimeout(function () {
  console.log('2');
}, 100);
console.log('3');

// Synchronous callback
function printImmediately(print) {
  print();
}
printImmediately(() => console.log('hello'));

// Asynchronous callback
function printWithDelay(print, timeout) {
  setTimeout(print, timeout);
}
printWithDelay(() => console.log('async callback'), 100);

// Callback Hell
class UserStorage {
  loginUser(id, password, onSuccess, onError) {
    setTimeout(() => {
      if (
        (id === 'knightofl' && password === 'honor') ||
        (id === 'lp3s' && password == 'rich')
      ) {
        onSuccess(id);
      } else {
        onError(new Error('id not found'));
      }
    }, 2000);
  }

  getRoles(user, onSuccess, onError) {
    setTimeout(() => {
      if (user === 'knightofl') {
        onSuccess({ name: 'knightofl', role: 'admin' });
      } else {
        onError(new Error('no access'));
      }
    }, 1000);
  }
}

const userStorage = new UserStorage();
const id = prompt('enter your id');
const password = prompt('enter your password');
userStorage.loginUser(
  id,
  password,
  (user) => {
    userStorage.getRoles(
      user,
      (userWithRole) => {
        alert(
          `Hello ${userWithRole.name}, you have a ${userWithRole.role} role.`
        );
      },
      (error) => {
        console.log(error);
      }
    );
  },
  (error) => {}
);
