const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : `${__dirname}/input.txt`;

let input = fs.readFileSync(filePath, "utf-8").trim().split("\n");
