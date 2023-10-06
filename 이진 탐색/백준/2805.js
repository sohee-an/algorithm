const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
const N = +input[0].split(" ")[0];
const M = +input[0].split(" ")[1];

const treeArray = input[1].split(" ").map((i) => Number(i));

let start = 0;
let end = treeArray.reduce((a, b) => Math.max(a, b));
let answer = 0;

while (start <= end) {
  let mid = parseInt((start + end) / 2);
  let total = 0;

  for (x of treeArray) {
    if (x > mid) {
      total += x - mid;
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
