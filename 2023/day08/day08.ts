/** Solutions to day 8 of advent of code 2023. **/
import * as fs from 'fs';
import { graph, getStepsTraversingMap } from './traverseGraph'

// Input reading.
let directionsMap: string = '';
let nodeData: string[] = [];
const inputData = fs.readFileSync('./input.txt', 'utf-8'); {
    const inputArray: string[] = inputData.split("\r\n");
    inputArray.forEach((line) => {
        const inputWords: string[] = line.replace(/[,=()]/g, '').split(" ");
        if (inputWords.length == 1 && inputWords[0] != '') {
            directionsMap = inputWords[0];
        }

        if (inputWords.length > 1) {
            graph.insert({ name: inputWords[0], L: inputWords[2], R: inputWords[3] });
            nodeData.push(inputWords[0]);
        }
    });
}

// For part 2 we have way too many iterations so instead of doing the
// traversal in the naive way we find the size of the loops for each start 
// position and find the smallest possible number of loops we can do to get
// to a Z-value for all the other nodes as well. This approach works well
// also for the case of one single traversal as in part 1.
const steps: number = getStepsTraversingMap("AAA", "ZZZ", nodeData, graph, directionsMap);
console.log("Number of steps for part 1 = %d", steps);

const ghostSteps: number = getStepsTraversingMap("A", "Z", nodeData, graph, directionsMap);
console.log("Number of steps for part 2 = %d", ghostSteps);
