const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim();

let inputarray = input.split("");

inputarray.sort((a, b) => b - a);
console.log(inputarray.join(""));
