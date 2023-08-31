const input = require("fs")
  .readFileSync("/dev/stdin", "utf-8")
  .trim()
  .split("\n");
//갯수
const arrayNumber = input.shift();
// 중복제거;
const uniqueWords = new Set(input);
const uniqueWordsArray = Array.from(uniqueWords).sort((a, b) => {
  // 길이가 같으면 사전 순으로 정렬
  if (a.length === b.length) {
    return a.localeCompare(b);
  }
  // 길이가 다르면 길이를 기준으로 정렬
  return a.length - b.length;
});

for (let i = 0; i < uniqueWordsArray.length; i++) {
  console.log(uniqueWordsArray[i]);
}
