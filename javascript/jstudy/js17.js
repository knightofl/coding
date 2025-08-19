'use strict'

const obj = {
  value: 42,
  getValue: () => {
    console.log(this.value);
  }
};

obj.getValue(); // undefined
