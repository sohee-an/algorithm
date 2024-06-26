const input = require("fs")
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split("\n");

const arrayNumber = input.shift("");
const parsedInput = input.map((item) => item.split(" "));

parsedInput.sort((a, b) => {
  if (a[1] === b[1]) {
    return a[0] - b[0];
  } else {
    return a[1] - b[1];
  }
});
const outputArray = parsedInput.map((item) => item.join(" "));

// 배열을 줄 바꿈으로 연결하여 출력
console.log(outputArray.join("\n"));
