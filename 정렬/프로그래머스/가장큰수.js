function solution(numbers) {
  var answer = "";

  numbers.sort((a, b) => {
    const num1 = String(a);
    const num2 = String(b);
    // 두 숫자를 합친 문자열을 비교
    if (num1 + num2 > num2 + num1) {
      return -1;
    } else if (num1 + num2 < num2 + num1) {
      return 1;
    } else {
      return 0;
    }
  });
  answer = numbers.join("");

  console.log("aa", answer[0]);

  // 만약 0으로 시작하는 숫자라면 "0"으로 처리
  if (answer[0] === "0") {
    return "0";
  }

  return answer;
}

console.log(solution[(3, 30, 34, 5, 9)]);
