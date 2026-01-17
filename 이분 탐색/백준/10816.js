const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");

const n = parseInt(input[0]);
const n_arr = input[1].split(" ").map((i) => Number(i));

const m = parseInt(input[2]);
const m_arr = input[3].split(" ").map((i) => Number(i));

const myMap = new Map();

for (let i = 0; i < n; i++) {
  const num = n_arr[i];
  if (myMap.has(num)) {
    myMap.set(num, myMap.get(num) + 1);
  } else {
    myMap.set(num, 1);
  }
}

for (let i = 0; i < m; i++) {
  const num = m_arr[i];
  if (myMap.has(num)) {
    m_arr[i] = myMap.get(num);
  } else {
    m_arr[i] = 0;
  }
}

const answer = m_arr.join(" ");
console.log(answer);
