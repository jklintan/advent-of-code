/** Solutions to day 6 of advent of code 2023. **/
import * as fs from 'fs';

// Get all possible ways to win and beat the record per race and multiply together.
function getPossibleWinWaysProduct(time_data: number[], record_distance_data: number[]): number {
	let possibleWinWaysPerRace: number[] = [];
	for (let raceId = 0; raceId < record_distance_data.length; raceId++) {
		const raceTime: number = time_data[raceId];
		const currentRecord: number = record_distance_data[raceId];
		let possibleWinWaysCurrentRace: number = 0;
		for (let buttonHold = 0; buttonHold < raceTime + 1; buttonHold++) {
			const speed: number = buttonHold;
			const distance: number = (raceTime - buttonHold) * speed;
			if (distance > currentRecord) {
				possibleWinWaysCurrentRace += 1;
			}
		}
		possibleWinWaysPerRace.push(possibleWinWaysCurrentRace);
	}
	return possibleWinWaysPerRace.reduce((a, b) => a * b, 1);
}

let time_data: number[] = [];
let record_distance_data: number[] = [];
const inputData = fs.readFileSync('./input.txt', 'utf-8'); {
	const inputArray: string[] = inputData.split("\r\n");
	inputArray.forEach((line) => {
		const inputWords: string[] = line.replace(':', '').split(" ");
		if (inputWords[0] == "Time") {
			inputWords.splice(1).filter(Number).forEach((word) => {
				time_data.push(parseInt(word));
			});
		}
		if (inputWords[0] == "Distance") {
			inputWords.splice(1).filter(Number).forEach((word) => {
				record_distance_data.push(parseInt(word));
			});
		}
	});
}

console.log("Answer part 1 = %d", getPossibleWinWaysProduct(time_data, record_distance_data));

// Convert the input to be one single race.
let time: string = "";
let distance: string = "";
for (let i = 0; i < time_data.length; i++) {
	time += time_data[i].toString();
	distance += record_distance_data[i].toString();
}

console.log("Answer part 2 = %d", getPossibleWinWaysProduct([Number(time)], [Number(distance)]));
