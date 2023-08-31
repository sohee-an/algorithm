const input = require("fs")
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split("\n")
  .map((item) => parseInt(item));

const iter = input.shift();

// Set을 사용하여 중복을 제거합니다.
input.sort((a, b) => a - b);

for (let i = 0; i < iter; i++) {
  console.log(input[i]);
}
