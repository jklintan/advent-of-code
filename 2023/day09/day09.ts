/** Solutions to day 9 of advent of code 2023. **/
import * as fs from 'fs';

// Extrapolate to the right and get the top most value for the sequence.
function getTopExtrapolatedValueRight(currentSequences: any[]): number {
    let currRowIdx: number = currentSequences.length - 1;
    let padValue: number = 0;
    while (currRowIdx != 0) {
        currentSequences[currRowIdx].push(padValue);
        currRowIdx -= 1;
        const row: number[] = currentSequences[currRowIdx];
        const lastElementIdx: number = row.length - 1;
        padValue = row[lastElementIdx] + padValue;
        currentSequences[currRowIdx].push(padValue);
    }
    return currentSequences[0][currentSequences[0].length - 1];
}

// Extrapolate to the left and get the top most value for the sequence.
function getTopExtrapolatedValueLeft(currentSequences: any[]): number {
    let currRowIdx: number = currentSequences.length - 1;
    let padValue: number = 0;
    while (currRowIdx != 0) {
        currRowIdx -= 1;
        const row: number[] = currentSequences[currRowIdx];
        padValue = row[0] - padValue;
        currentSequences[currRowIdx].unshift(padValue);
    }
    return currentSequences[0][0];
}

// Input reading.
let inputSequences: any[] = [];
const inputData = fs.readFileSync('./input.txt', 'utf-8'); {
    const inputArray: string[] = inputData.split("\r\n");
    inputArray.forEach((line) => {
        const inputNumbers: number[] = line.split(" ").map(i => Number(i));
        inputSequences.push(inputNumbers);
    });
}

// Add differences and then find top right
// and top left most padded value when
// extending the series.
let sumPart1 = 0;
let sumPart2 = 0;
for (let i = 0; i < inputSequences.length; i++) {
    let currentSequences: any[] = [];
    currentSequences.push(inputSequences[i]);

    let difference: number[] = inputSequences[i];
    let index: number = 0;
    let currentNumbers: number[] = inputSequences[i];
    while (!difference.every(item => item === 0)) {
        difference = [];
        currentNumbers = currentSequences[index];
        for (let j = 0; j < currentNumbers.length - 1; j++) {
            difference.push(currentNumbers[j + 1] - currentNumbers[j]);
        }
        currentSequences.push(difference);
        index += 1;
    }

    // Part 1
    sumPart1 += getTopExtrapolatedValueRight(structuredClone(currentSequences));

    // Part 2
    sumPart2 += getTopExtrapolatedValueLeft(structuredClone(currentSequences));
}

console.log("Sum part 1 = %d", sumPart1);
console.log("Sum part 2 = %d", sumPart2);
