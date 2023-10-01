const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
const N = +input[0].split(" ")[0];
const M = +input[0].split(" ")[1];

const arr = [];
for (let i = 0; i < N; i++) {
  arr.push(+input[i + 1]);
}
let answer = 0;
let start = 0;
let end = arr.reduce((a, b) => Math.max(a, b));

while (start <= end) {
  let mid = parseInt((start + end) / 2);
  let total = 0;
  for (x of arr) {
    if (x > mid) {
      total += x / mid;
    }
  }
  if (total < M) {
    end = mid - 1;
  } else {
    answer = mid;
    start = mid + 1;
  }
}
console.log(answer);
