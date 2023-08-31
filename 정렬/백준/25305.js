const input = require("fs")
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split("\n");

// 첫째줄
let input1 = input[0].split(" ");
//  수상자 숫자
const member = input1[1];
// 두번째 줄

const grad = input[1].split(" ");

const answer = grad.sort((a, b) => b - a)[member - 1];
console.log(answer);
