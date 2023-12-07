/** Solutions to day 7 of advent of code 2023. **/
import * as fs from 'fs';
import * as day07Functionality from './day07Functionality';

// Input reading.
let handData: string[] = [];
let bidData: number[] = [];
const inputData = fs.readFileSync('./input.txt', 'utf-8'); {
	const inputArray: string[] = inputData.split("\r\n");
	inputArray.forEach((line) => {
		const inputWords: string[] = line.replace(':', '').split(" ");
		handData.push(inputWords[0]);
		bidData.push(Number(inputWords[1]));
	});
}

// Part 1
const playCardsPart1: string[] = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"];
const types: any[] = day07Functionality.sortData(handData, playCardsPart1);

// Sort each type according to the second criteria, then go through
// all and calculate the bid times ranking in order. Using the highest
// ranking first and then going lower.
const winningHands: number = day07Functionality.getTotalWinnings(types, handData, bidData, playCardsPart1);
console.log("The total winnings for part 1 = %d", winningHands);

// Part 2
const playCardsPart2: string[] = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"];
const typesWithJokers: any[] = day07Functionality.sortData(handData, playCardsPart2, true);

// Sort each type according to the second criteria, then go through
// all and calculate the bid times ranking in order. Using the highest
// ranking first and then going lower.
const winningHandsWithJoker: number = day07Functionality.getTotalWinnings(typesWithJokers, handData, bidData, playCardsPart2);
console.log("The total winnings for part 2 = %d", winningHandsWithJoker);
