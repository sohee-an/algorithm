const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
const arrayNumber = input[0];

let n = Number(arrayNumber.split(" ")[0]);
let k = Number(arrayNumber.split(" ")[1]);
let arr = [];
for (let i = 1; i <= n; i++) arr.push(Number(input[i]));

let cnt = 0;

for (let i = n - 1; i >= 0; i--) {
  //   console.log(arr[i]);

  cnt += parseInt(k / arr[i]);
  //   console.log("cnt", cnt);
  k %= arr[i];
}

console.log(cnt);
