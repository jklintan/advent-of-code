/** Solutions to day 11 of advent of code 2023. **/
import * as fs from "fs";

// Get index range as an array between start and stop per step.
function arrayRange(start: number, stop: number, step: number): number[] {
  return Array.from({ length: (stop - start) / step + 1 }, (_, index) => start + index * step);
}

// Get shortest path between all galaxy paths.
function getShortestGalaxyPath(
  numGalaxies: number,
  galaxyCountMap: number[],
  expandableRows: number[],
  expandableColumns: number[],
  expansionRate: number
): number {
  let sum: number = 0;
  for (let i = 0; i < numGalaxies; i++) {
    const x: number = galaxyCountMap[2 * i];
    const y: number = galaxyCountMap[2 * i + 1];
    for (let j = i + 1; j < numGalaxies; j++) {
      const xc: number = galaxyCountMap[2 * j];
      const yc: number = galaxyCountMap[2 * j + 1];
      const shortestPath = Math.abs(xc - x) + Math.abs(yc - y);
      const rangeRows: number[] = x <= xc ? arrayRange(x, xc, 1) : arrayRange(xc, x, 1);
      const rangeCols: number[] = y <= yc ? arrayRange(y, yc, 1) : arrayRange(yc, y, 1);
      const passingRows = expandableRows.filter((value) => rangeRows.includes(value)).length;
      const passingCols = expandableColumns.filter((value) => rangeCols.includes(value)).length;
      sum += shortestPath + (passingRows + passingCols) * (expansionRate - 1);
    }
  }
  return sum;
}

// Input reading.
let inputGalaxy: any[] = [];
const inputData = fs.readFileSync("./input.txt", "utf-8");
{
  const inputArray: string[] = inputData.split("\r\n");
  inputArray.forEach((line) => {
    const inputLine: string[] = line.split("");
    inputGalaxy.push(inputLine);
  });
}

// Get all rows and columns which has no galaxies and should
// be used for expansion.
let expandableRows: number[] = [];
for (let index = 0; index < inputGalaxy.length; index++) {
  if (inputGalaxy[index].filter((x) => x === ".").length == inputGalaxy[index].length) {
    expandableRows.push(index);
  }
}

let expandableColumns: number[] = [];
for (let i = 0; i < inputGalaxy[0].length; i++) {
  let noGalaxies: boolean = true;
  for (let j = 0; j < inputGalaxy.length; j++) {
    if (inputGalaxy[j][i] == "#") {
      noGalaxies = false;
      break;
    }
  }
  if (noGalaxies) {
    expandableColumns.push(i);
  }
}

// Count the number of galaxies and get
// the indices for them.
let numGalaxies: number = 0;
let galaxyIndicesMap: number[] = [];
for (let i = 0; i < inputGalaxy.length; i++) {
  numGalaxies += inputGalaxy[i].filter((x) => x === "#").length;
  for (let j = 0; j < inputGalaxy[0].length; j++) {
    if (inputGalaxy[i][j] == "#") {
      galaxyIndicesMap.push(i, j);
    }
  }
}

console.log(
  "Shortest path for part 1 = %d",
  getShortestGalaxyPath(numGalaxies, galaxyIndicesMap, expandableRows, expandableColumns, 2)
);
console.log(
  "Shortest path for part 2 = %d",
  getShortestGalaxyPath(numGalaxies, galaxyIndicesMap, expandableRows, expandableColumns, 1e6)
);
