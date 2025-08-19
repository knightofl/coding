'use strict';

const obj = {
    value: 42,
    normalFunc: function() {
        console.log(this.value);  // 42
    },
    arrowFunc: () => {
        console.log(this.value);  // undefined
    }
};

obj.normalFunc(); // 42
obj.arrowFunc();  // undefined (화살표 함수는 `this`를 바인딩하지 않음)
