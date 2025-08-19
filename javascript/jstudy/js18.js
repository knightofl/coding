'use strict'

// 1. 전역 컨텍스트
console.log("1. 전역:", this);

// 2. 일반 함수 호출
function normalFunc() {
  console.log("2. 일반 함수:", this);
}
normalFunc();

// 3. 객체 메서드
const obj = {
  name: "Alice",
  sayHi: function() {
    console.log("3. 객체 메서드:", this);
  }
};
obj.sayHi();

// 4. 생성자 함수
function Person(name) {
  this.name = name;
  console.log("4. 생성자 함수:", this);
}
new Person("Bob");

// 5. call/apply/bind
function greet() {
  console.log("5. call/apply/bind:", this);
}
greet.call({ lang: "Korean" });
greet.apply({ lang: "English" });
const bound = greet.bind({ lang: "Japanese" });
bound();

// 6. 화살표 함수
const arrowObj = {
  value: 42,
  arrow: () => {
    console.log("6. 화살표 함수:", this);
  }
};
arrowObj.arrow();

// 7. 화살표 함수 (외부 스코프 상속 확인)
function outer() {
  return () => {
    console.log("7. 화살표(외부 스코프):", this);
  };
}
const arrowTest = outer.call({ outerValue: 99 });
arrowTest();