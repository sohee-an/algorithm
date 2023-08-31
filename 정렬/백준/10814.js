const input = require("fs")
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split("\n");

const arrayNumber = input.shift();
//  나이순으로 정렬을 하되 나이가 같으면 가입한 순으로 정렬해라
//그럴려면 정렬을 일단 두고 하나씩 비교를 해야되나?

// 배열로 만들기
const defaultArray = input.map((item) => {
  return item.split(" ");
});

defaultArray.sort((a, b) => {
  // 0번째 요소가 같으면 1번째 요소로 정렬
  if (a[0] === b[0]) {
    return a[1] - b[1];
  }
  // 0번째 요소로 정렬
  return a[0] - b[0];
}); // 정렬된 배열 출력
for (let i = 0; i < defaultArray.length; i++) {
  console.log(defaultArray[i].join(" "));
}
