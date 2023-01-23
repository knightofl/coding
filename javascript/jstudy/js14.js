'use strict';

class Counter {
  constructor(runIf) {
    this.counter = 0;
    this.callback = runIf;
  }

  increase() {
    this.counter++;
    console.log(this.counter);
    this.callback && this.callback(this.counter);
  }
}

function even(num) {
  if (num % 2 === 0) {
    console.log('even');
  }
}

const obj = new Counter(even);
// const obj = new Counter();
obj.increase();
obj.increase();
obj.increase();
obj.increase();
obj.increase();
