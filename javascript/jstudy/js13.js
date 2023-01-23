'use strtict';

// async & await
// clear style of using promise

// promise
function fetchUser1() {
  return new Promise((resolve, reject) => {
    // do network request in 10 secs...
    resolve('knightofl');
  });
}

const user1 = fetchUser1();
user1.then(console.log);

async function fetchUser2() {
  // do network request in 10 secs...
  return 'lupin3se';
}

const user2 = fetchUser2();
user2.then(console.log);

// aawait
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function getApple() {
  await delay(2000);
  return '🍎';
}

async function getBanana() {
  await delay(1000);
  return '🍌';
}

function pickFruits1() {
  return getApple().then((apple) => {
    return getBanana().then((banana) => `${apple} + ${banana} 1`);
  });
}
pickFruits1().then(console.log);

async function pickFruits2() {
  const apple = await getApple();
  const banana = await getBanana();
  return `${apple} + ${banana} 2`;
}

pickFruits2().then(console.log);

async function pickFruits3() {
  const applePromise = getApple();
  const bananaPromise = getBanana();
  const apple = await applePromise;
  const banana = await bananaPromise;
  return `${apple} + ${banana} 3`;
}

pickFruits3().then(console.log);

// useful Promise APIs
function pickFruits4() {
  return Promise.all([getApple(), getBanana()]).then(
    (fruits) => fruits.join(' + ') + ' 4'
  );
}
pickFruits4().then(console.log);

function pickOnlyOne() {
  return Promise.race([getApple(), getBanana()]);
}
pickOnlyOne().then(console.log);
