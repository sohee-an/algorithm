const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
const arrayNumber = Number(input.shift());
let array = [];
input.map((i) => {
  return array.push(Number(i));
});
let answer = 0;
for (let i = arrayNumber - 1; i > arrayNumber - 1; i--) {}

console.log(array);
