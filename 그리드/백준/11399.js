const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");

const arrayNumber = Number(input.shift());
const array = input[0].split(" ");

const inputArray = array
  .sort((a, b) => {
    return a - b;
  })
  .map((i) => Number(i));

let answer = 0;
let sum = [];
sum.push(inputArray[0]);

for (let i = 1; i < arrayNumber; i++) {
  sum[i] = inputArray[i] + sum[i - 1];
}

for (let i = 0; i < sum.length; i++) {
  answer += sum[i];
}

console.log(answer);
