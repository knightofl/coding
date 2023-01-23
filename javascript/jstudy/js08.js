'use strict';

// Q1. make a string out of an array
{
  const fruits = ['apple', 'banana', 'orange'];
  fruits.forEach((fruit) => console.log(fruit));
  console.log(fruits.toString());
  console.log(fruits.join());
}

// Q2. make an array out of a string
{
  const fruits = '🍎, 🥝, 🍌, 🍒';
  const fruits2 = fruits.split(', ');
  console.log(fruits2);
}

// Q3. make this array look like this: [5, 4, 3, 2, 1]
{
  const array = [1, 2, 3, 4, 5];
  array.sort();
  array.reverse();
  console.log(array);
}

// Q4. make new array without the first two elements
{
  const array1 = [1, 2, 3, 4, 5];
  array1.splice(0, 2);
  console.log(array1);

  const array2 = [1, 2, 3, 4, 5];
  const array3 = array2.slice(2);
  console.log(array2);
  console.log(array3);
}

class Student {
  constructor(name, age, enrolled, score) {
    this.name = name;
    this.age = age;
    this.enrolled = enrolled;
    this.score = score;
  }
}
const students = [
  new Student('A', 29, true, 45),
  new Student('B', 28, false, 80),
  new Student('C', 30, true, 90),
  new Student('D', 40, false, 66),
  new Student('E', 18, true, 88),
];

// Q5. find a student with the score 90
{
  console.log(students);
  students.forEach((std) => {
    if (std.score === 90) {
      console.log(std);
    }
  });

  const result1 = students.find(function (std) {
    return std.score === 90;
  });
  console.log(result1);

  const result2 = students.find((std) => std.score === 90);
  console.log(result2);
}

// Q6. make an array of enrolled students
{
  const result1 = new Array();
  students.forEach((std) => {
    if (std.enrolled === true) {
      result1.push(std);
    }
  });
  console.log(result1);

  const result2 = students.filter((std) => std.enrolled);
  console.log(result2);
}

// Q7. make an array containing only the students' scores
// result should be: [45, 80, 90, 66, 88]
{
  const result1 = new Array();
  students.forEach((std) => result1.push(std.score));
  console.log(result1);

  const result2 = students.map((std) => std.score);
  console.log(result2);
}

// Q8. check if there is a student with the score lower than 50
{
  students.forEach((std) => {
    if (std.score < 50) {
      console.log(std.name);
    }
  });

  const result1 = students.some((std) => std.score < 50);
  console.log(result1);

  const result2 = students.every((std) => std.score >= 50);
  console.log(result2);
}

// Q9. compute students' average score
{
  let sum1 = 0;
  students.forEach((std) => (sum1 += std.score));
  console.log(sum1 / students.length);

  students.reduce((previous, current) => {
    console.log('--------------');
    console.log(previous);
    console.log(current);
    return current;
  });

  const sum2 = students.reduce((previous, current) => {
    return previous + current.score;
  }, 0);
  console.log(sum2 / students.length);

  const sum3 = students.reduce(
    (previous, current) => previous + current.score,
    0
  );
  console.log(sum3 / students.length);
}

// Q10. make a string containing all the scores
// result should be: '45, 80, 90, 66, 88'
{
  const result1 = new Array();
  students.forEach((std) => result1.push(std.score));
  console.log(result1.toString());

  const result2 = students.map((std) => std.score).join();
  console.log(result2);
}

// Bonus! do Q10 sorted in ascending order
// result should be: '45, 66, 80, 88, 90'
{
  const result1 = new Array();
  students.forEach((std) => result1.push(std.score));
  result1.sort();
  console.log(result1.toString());

  const result2 = students
    .map((std) => std.score)
    .sort()
    .join();
  console.log(result2);

  const result3 = students
    .map((std) => std.score)
    .sort((a, b) => b - a)
    .join();
  console.log(result3);
}
