/** Solutions to day 5 of advent of code 2023. **/
import * as fs from 'fs';

// Input interface for storing
// the maps and the ranges.
interface Map {
    name: string;
    ranges: number[];
}

// From a given seed, find the corresponding location.
function findLocation(seed: number, seedData: Map[]): number {
    let src: number = seed;
    for (let i = 1; i < seedData.length; i++) {
        const conversionElements: number[] = seedData[i].ranges;
        const numRanges: number = conversionElements.length / 3;
        for (let j: number = 0; j < numRanges; j++) {
            const dstRangeStart: number = conversionElements[3 * j];
            const srcRangeStart: number = conversionElements[3 * j + 1];
            const range: number = conversionElements[3 * j + 2];

            if (srcRangeStart + range > src && src >= srcRangeStart) {
                const difference: number = src - srcRangeStart;
                src = dstRangeStart + difference;
                break;
            }
        }
    }
    return src;
}

// From a given location, find the corresponding seed.
function findSeed(location: number, seedData: Map[]): number {
    let dst: number = location;
    for (let i = seedData.length - 1; i > 0; i--) {
        const conversionElements: number[] = seedData[i].ranges;
        const numRanges: number = conversionElements.length / 3;
        for (let j: number = 0; j < numRanges; j++) {
            const dstRangeStart: number = conversionElements[3 * j];
            const srcRangeStart: number = conversionElements[3 * j + 1];
            const range: number = conversionElements[3 * j + 2];

            if (dst >= dstRangeStart && dstRangeStart + range > dst) {
                const difference: number = dst - dstRangeStart;
                dst = srcRangeStart + difference;
                break;
            }
        }
    }
    return dst;
}

// Get the seed which corresponds to the lowest possible location.
function getSeedWithLowestPossibleLocation(inputSeeds: Map[], startVal: number, endVal: number): number {
    const numRanges: number = inputSeeds[0].ranges.length / 2;
    for (let index = startVal; index < endVal; index++) {
        const element: number = findSeed(index, inputSeeds);
        for (let index = 0; index < numRanges; index++) {
            const value: number = inputSeeds[0].ranges[2 * index];
            const range: number = inputSeeds[0].ranges[2 * index + 1];

            if (element >= value && element <= value + range) {
                return element;
            }
        }
    }
    return -1;
}

// Get the maximum possible seed in input so we can use it for a cap.
function getMaximumSeed(seeds: number[]): number {
    const numRanges: number = seeds.length / 2;
    let maxValue: number = 0;
    for (let index = 0; index < numRanges; index++) {
        const value: number = inputSeeds[0].ranges[2 * index];
        const range: number = inputSeeds[0].ranges[2 * index + 1];

        if (value + range > maxValue) {
            maxValue = value + range;
        }
    }
    return maxValue;
}

let inputSeeds: Map[] = [];
const inputData = fs.readFileSync('./input.txt', 'utf-8'); {
    const inputArray: string[] = inputData.split("\r\n");
    let currentMap: Map = { name: "", ranges: [] };
    inputArray.forEach((line) => {
        const inputWords: string[] = line.replace(':', '').split(" ");

        if (inputWords[0] == "seeds") {
            currentMap.name = "seeds";
            inputWords.splice(1).forEach((word) => {
                currentMap.ranges.push(parseInt(word));
            });
        } else if (inputWords[1] == "map") {
            currentMap.name = inputWords[0];
        } else {
            inputWords.forEach((word) => {
                currentMap.ranges.push(parseInt(word));
            });
        }

        if (currentMap.name != "" && line == "") {
            currentMap.ranges.pop();
            inputSeeds.push(structuredClone(currentMap));
            currentMap.name = "";
            currentMap.ranges = [];
        }
    });

    // Add the last entry.
    inputSeeds.push(structuredClone(currentMap));
}

// Part 1
// Enough to simply convert and find the corresponding
// location of each seed by going through the maps.
// We keep the lowest found location.
const seedNumbers: number[] = inputSeeds[0].ranges;
var lowestLocation: number = 1e16;
seedNumbers.forEach((number) => {
    const location: number = findLocation(number, inputSeeds);
    if (location < lowestLocation) {
        lowestLocation = location;
    }
});
console.log("Lowest location part 1 = %d", lowestLocation);

// Part 2
// Too many seeds to go through every single one
// in all of the ranges, so instead we turn the
// problem around and go through locations from 0
// and upwards until we find a seed which is within
// the range of possible seeds. We set end value to
// be the maximum possible seed in the input.
const maxValue: number = getMaximumSeed(inputSeeds[0].ranges);
const bestSeed: number = getSeedWithLowestPossibleLocation(inputSeeds, 0, maxValue);
lowestLocation = findLocation(bestSeed, inputSeeds);
console.log("Lowest location part 2 = %d", lowestLocation);
