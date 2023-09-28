const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim();
const length = parseInt(input);

function factorial(N) {
  // 기저 조건: 0! 또는 1!은 항상 1이므로 1을 반환
  if (N === 0 || N === 1) {
    return 1;
  } else {
    // N! = N * (N-1)!
    return N * factorial(N - 1);
  }
}

console.log(factorial(length));
