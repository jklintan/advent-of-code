/** Solutions to day 10 of advent of code 2023. **/
import * as fs from 'fs';
import * as utils from './utils';

// Input reading.
let inputSequences: any[] = [];
let symbols: any[] = []
const inputData = fs.readFileSync('./input.txt', 'utf-8'); {
    const inputArray: string[] = inputData.split("\r\n");
    inputArray.forEach((line) => {
        const inputLine: string[] = line.split("");
        for (let index = 0; index < inputLine.length; index++) {
            symbols.push(inputLine[index]);
        }
        inputSequences.push(inputLine);
    });
}

// Build graph and adjacency (edges) for all input,
// and make sure we have all things needed to start
// traversing the map.
const adjacency: any[] = utils.buildAdjacency(symbols, inputSequences);
const coords: number[] = utils.getStartPosition(symbols, inputSequences, 'S');
const rows: number = inputSequences.length;
const cols: number = inputSequences[0].length;
const surroundings = utils.getSurroundings(coords[0], coords[1], rows, cols)
let startAdjacency: number[] = [];
let startSymbols: string[] = [];
for (let index = 0; index < surroundings.length; index++) {
    if (symbols[surroundings[index]] != '.') {
        startSymbols.push(symbols[surroundings[index]]);
        startAdjacency.push(surroundings[index]);
    }
}

// Find the length of the cycle in the graph.
// Our wanted value is half of that (farthest
// away from the start position in steps).
let lengthOfCircle: number = 1
let foundSolution: boolean = false;
let mapVisited: number[] = [];
let mapLoop: string[] = [];
const startIndex: number = utils.toFlatIndex(coords[0], coords[1], cols);
for (let index = 0; index < startAdjacency.length; index++) {
    let goTo: number = startAdjacency[index];
    let cameFrom: number = startIndex;
    lengthOfCircle = 1;

    // Binary map with 1s where the circle is, 0s otherwise.
    mapVisited = new Array(symbols.length).fill(0);
    mapVisited[cameFrom] = 1;

    // Map which keeps all symbols that are part of the circle
    // intact but turns everything else into '.'s.
    mapLoop = new Array(symbols.length).fill('.');
    mapLoop[cameFrom] = symbols[cameFrom];

    while (goTo != startIndex) {
        mapVisited[goTo] = 1;
        mapLoop[goTo] = symbols[goTo];

        // Remove where we came from to easily get the next one.
        let currentAdjacency: number[] = structuredClone(adjacency[goTo]);
        currentAdjacency[cameFrom] = 0;

        // Not part of the circle if either no adjacency
        // or if we have more than 1 path left to take.
        const numOnes: number = currentAdjacency.filter(x => x === 1).length;
        if (numOnes > 1 || numOnes == 0) {
            break;
        }

        cameFrom = goTo;
        goTo = currentAdjacency.indexOf(1);
        lengthOfCircle += 1;
        if (goTo == startIndex) {
            foundSolution = true;
        }
    }

    if (goTo == startIndex) {
        break;
    }
}

console.log("Steps farthest from the starting position = %d", lengthOfCircle / 2)

// Part 2, start with flood filling from the edges.
for (let index = 0; index < cols; index++) {
    utils.floodFill(mapLoop, 0, index, rows, cols, '.', '0');
    utils.floodFill(mapLoop, rows - 1, index, rows, cols, '.', '0');
}

for (let index = 0; index < rows; index++) {
    utils.floodFill(mapLoop, index, 0, rows, cols, '.', '0');
    utils.floodFill(mapLoop, index, cols - 1, rows, cols, '.', '0');
}

// Traverse the loop, if we traverse it clockwise, all parts that are
// to the right of the loop will be within the loop itself. We can't
// be sure that we are traversing clockwise though so do the traversal
// for both clockwise and counter-clockwise and present the options.
let options: number[] = [];
for (let index = 0; index < startAdjacency.length; index++) {
    foundSolution = false;
    let goTo: number = startAdjacency[index];
    let cameFrom: number = startIndex;
    let currentMap: string[] = structuredClone(mapLoop);
    while (goTo != startIndex) {
        const xIndex: number = Math.floor(goTo / cols);
        const yIndex: number = goTo % cols;
        if (xIndex > 0 && yIndex > 0 && xIndex < rows && yIndex < cols) {
            switch (currentMap[goTo]) {
                case '|':
                    if (cameFrom < goTo) {
                        if (currentMap[goTo - 1] == '.') { // Going down.
                            utils.floodFill(currentMap, xIndex, yIndex - 1, rows, cols, '.', 'X');
                        }
                    } else {
                        if (currentMap[goTo + 1] == '.') { // Going up.
                            utils.floodFill(currentMap, xIndex, yIndex + 1, rows, cols, '.', 'X');
                        }
                    }
                    break;
                case '-':
                    if (cameFrom < goTo) {
                        if (currentMap[goTo + cols] == '.') { // Going right.
                            utils.floodFill(currentMap, xIndex + 1, yIndex, rows, cols, '.', 'X');
                        }
                    } else {
                        if (currentMap[goTo - cols] == '.') { // Going left.
                            utils.floodFill(currentMap, xIndex - 1, yIndex, rows, cols, '.', 'X');
                        }
                    }
                    break;
                case 'F':
                    // Only check if travelling left, otherwise we don't
                    // need to care, tile before & after takes care of it.
                    if (Math.abs(cameFrom - goTo) == 1) {
                        if (currentMap[goTo - cols] == '.') {
                            utils.floodFill(currentMap, xIndex - 1, yIndex, rows, cols, '.', 'X');
                        }
                        if (currentMap[goTo - cols - 1] == '.') {
                            utils.floodFill(currentMap, xIndex - 1, yIndex - 1, rows, cols, '.', 'X');
                        }
                        if (currentMap[goTo - 1] == '.') {
                            utils.floodFill(currentMap, xIndex, yIndex - 1, rows, cols, '.', 'X');
                        }
                    }
                    break;
                case 'J':
                    // Only check if travelling right, otherwise we don't
                    // need to care, tile before & after takes care of it.
                    if (Math.abs(cameFrom - goTo) == 1) {
                        if (currentMap[goTo + cols] == '.') {
                            utils.floodFill(currentMap, xIndex + 1, yIndex, rows, cols, '.', 'X');
                        }
                        if (currentMap[goTo + cols + 1] == '.') {
                            utils.floodFill(currentMap, xIndex + 1, yIndex + 1, rows, cols, '.', 'X');
                        }
                        if (currentMap[goTo + 1] == '.') {
                            utils.floodFill(currentMap, xIndex, yIndex + 1, rows, cols, '.', 'X');
                        }
                    }
                    break;
                case '7':
                    // Only check if travelling up, otherwise we don't
                    // need to care, tile before & after takes care of it.
                    if (Math.abs(cameFrom - goTo) != 1) {
                        if (currentMap[goTo + 1] == '.') {
                            currentMap[goTo + 1] = 'X';
                        }
                        if (currentMap[goTo - cols + 1] == '.') {
                            currentMap[goTo - cols + 1] = 'X';
                        }
                        if (currentMap[goTo - cols] == '.') {
                            currentMap[goTo - cols] = 'X';
                        }
                    }
                    break;
                case '7':
                    // Only check if travelling down, otherwise we don't
                    // need to care, tile before & after takes care of it.
                    if (Math.abs(cameFrom - goTo) != 1) {
                        if (currentMap[goTo - 1] == '.') {
                            utils.floodFill(currentMap, xIndex, yIndex - 1, rows, cols, '.', 'X');
                        }
                        if (currentMap[goTo + cols - 1] == '.') {
                            utils.floodFill(currentMap, xIndex + 1, yIndex - 1, rows, cols, '.', 'X');
                        }
                        if (currentMap[goTo + cols] == '.') {
                            utils.floodFill(currentMap, xIndex + 1, yIndex, rows, cols, '.', 'X');
                        }
                    }
                    break;
                default:
                    break;
            }
        }
        let currentAdjacency: number[] = structuredClone(adjacency[goTo]);
        currentAdjacency[cameFrom] = 0;

        // Not part of the circle if either no adjacency
        // or if we have more than 1 path left to take.
        const numPairs: number = currentAdjacency.filter(x => x === 1).length;
        if (numPairs > 1 || numPairs == 0) {
            break;
        }

        cameFrom = goTo;
        goTo = currentAdjacency.indexOf(1);
        if (goTo == startIndex) {
            foundSolution = true;
            break;
        }
    }

    if (foundSolution) {
        options.push(currentMap.filter(x => x === 'X').length);
    }
}

console.log("The solutions is one of the two options: " + options[0] + " or " + options[1])
