const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
console.log("iinput", input);
const arrayNumber = input[0];

let firstArray = input[1].split(" ");
let secondArray = input[2].split(" ");
let answer = 0;

firstArray
  .sort((a, b) => {
    return a - b;
  })
  .map((i) => Number(i));
secondArray
  .sort((a, b) => {
    return a - b;
  })
  .map((i) => Number(i));

for (let i = 0; i < arrayNumber; i++) {
  answer += firstArray[i] * secondArray[i];
}
console.log(answer);
