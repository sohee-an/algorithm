const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");

// 총 회의실 시간
let number = input.shift();

input.sort((a, b) => {
  const a_array = a.split(" ");
  const b_array = b.split(" ");
  if (a_array[0] === b_array[0]) {
    return a - b;
  } else {
    return b - a;
  }
});
console.log("input", input);
