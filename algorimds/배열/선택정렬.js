const arr = [30, 50, 20, 89, 1, 21];

function selectedarr(arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] > arr[j]) {
        let firstindex = arr[i];
        arr[i] = arr[j];
        arr[j] = firstindex;
      }
    }
  }
  return arr;
}

console.log(selectedarr(arr));

// 리팩토링 코드
function selectionSort(arr) {
  const n = arr.length;
  for (let i = 0; i < n - 1; i++) {
    let minIndex = i;
    for (let j = i + 1; j < n; j++) {
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex !== i) {
      // Swap arr[i] and arr[minIndex]
      [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
    }
  }
  return arr;
}

console.log(selectionSort(arr));
