// 2차원 평면 위의 점 N개가 주어진다.
// 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한
// 다음 출력하는 프로그램을 작성하시오.

//  1. 문제가 이해가 안갔음
const input = require("fs")
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split("\n");

const arrayNumber = input.shift("");
const parsedInput = input.map((item) => item.split(" "));

parsedInput.sort((a, b) => {
  if (a[0] === b[0]) {
    return a[1] - b[1];
  } else {
    return a[0] - b[0];
  }
});
const outputArray = parsedInput.map((item) => item.join(" "));

// 배열을 줄 바꿈으로 연결하여 출력
console.log(outputArray.join("\n"));
