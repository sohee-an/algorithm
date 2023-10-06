const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
const arrayNumber = Number(input.shift());
const array = input[0].split(" ").map((i) => Number(i));
console.log("arr", arrayNumber);
console.log("arr", array);
