const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");

// 최소 비용을 계산을 해보자
//  각 거리에서 오는 최소비용

const max_num = Number(input.shift());
const distanceArray = input[0].split(" ").map((i) => Number(i));
const pricePerLitterArray = input[1].split(" ").map((i) => Number(i));
let answer = 0;

// 최소 비용 구하기 표대로 로직짜기
// 0 번째는 0
// 1번째 10 == 5 * 2 == 0번째 Price * 0번째에서 다음도시까지 거리

let minPriceToCitys = [];
minPriceToCitys.push(0); // 0번 도시까지 최소비용
minPriceToCitys.push(pricePerLitterArray[0] * distanceArray[0]); // 1번 도시까지 최소비용

let minPrice = -1;

for (let i = 2; i < max_num; ++i) {
  // i 번째에 도시까지 최소비용은
  // i-1 번쨰 최소비용 , i - 2번째 최소비용
  // 기대치를 비교
  // 남은 거리를 각각 더해줘보자

  // i가 2일 때,
  // totalPrice(i-1) == 10 + 남은거리 * 여기서의 기름값 (3)(2) == 10 + 6 == 16
  // tptalPrice(i-2) == 0 + 남은거리 * 여기서의 기름값 (2 + 3) ( 5) == 0 + 25

  // total price 구하는 법은, totalPrice(i-1) < totalPrice(i-2) ? 둘중 작은 i 번쨰를 구하고 거기서 남은 거리 및 비용을 더해서 현재를 만든다.
  // i 번째에서 남은거리 구하는 법은  배열을 부분순회해서 다 더함. 예를들어서,
  // a - b 까지의 남은 거리는, for(a~b) distanceArray의 합

  // i == 2, k == 0 0~2
  let remainDistanceA = 0;
  for (let k = i - 2; k < i; ++k) {
    remainDistanceA += distanceArray[k];
  }

  let remainDistanceK = 0;
  for (let k = i - 1; k < i; ++k) {
    remainDistanceK += distanceArray[k];
  }

  remainDistanceA + minPriceToCitys[k];

  // let currentPrice = 0;
  // if(minPrice <= -1 || minPrice < currentPrice)

  // expected price를 계산해보고 제일작은 값이 여기까지 도달하기 위한 최소 값 이다.
  // 가장 낮은 기름 값인 인덱스를 저장해 놓는게 중요함.. 사실..
}

// for (let i = 0; i < arrayNumber - 1; i++) {
//   if (i === 0) {
//     answer += firstArray[i] * secondArray[i];
//   } else {
//     if (secondArray[i] > secondArray[i + 1]) {
//       answer += secondArray[i + 1] * firstArray[i];
//       console.log("an", answer);
//     } else {
//       console.log("s", secondArray[i]);
//       answer += secondArray[i] * firstArray[i];
//       console.log("an2", answer);
//     }
//   }
// }

console.log("answer", answer);
