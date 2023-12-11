/** Utility functions. **/

// Converts a 2D index to a 1D.
export function toFlatIndex(i: number, j: number, cols: number): number {
	return cols * i + j
}

// Gets the start position in a map.
export function getStartPosition(symbols: string[], inputSequences: any[], sign: string): number[] {
	for (let i = 0; i < inputSequences.length; i++) {
		for (let j = 0; j < inputSequences[i].length; j++) {
			if (symbols[toFlatIndex(i, j, inputSequences[i].length)] == sign) {
				return [i, j];
			}
		}
	}
	return [];
}

// Gets the 4 surrounding items in a 2D map given an input index.
export function getSurroundings(i: number, j: number, rows: number, cols: number): number[] {
	let surroundings: number[] = []
	if (i != 0) {
		surroundings.push(toFlatIndex(i - 1, j, cols))
	}
	if (j != 0) {
		surroundings.push(toFlatIndex(i, j - 1, cols))
	}
	if (j != cols - 1) {
		surroundings.push(toFlatIndex(i, j + 1, cols))
	}
	if (i != rows - 1) {
		surroundings.push(toFlatIndex(i + 1, j, cols))
	}
	return surroundings
}

// Flood fill algorithm in 8 directions (4-neighbors + diagonal).
export function floodFill(image: any[], i: number, j: number, rows: number, cols: number, sign: string, newSign: string): any {
	// Stop at edges.
	if (i < 0 || j < 0 || i > rows - 1 || j > cols - 1) {
		return;
	}

	// Stop if we reach an index which indicates a stop.
	const idx = toFlatIndex(i, j, cols)
	if (image[idx] != sign) {
		return;
	}
	image[idx] = newSign;

	// Keep flood fill in all 8 adjacent directions.
	floodFill(image, i - 1, j, rows, cols, sign, newSign);
	floodFill(image, i + 1, j, rows, cols, sign, newSign);
	floodFill(image, i, j - 1, rows, cols, sign, newSign);
	floodFill(image, i, j + 1, rows, cols, sign, newSign);
	floodFill(image, i - 1, j - 1, rows, cols, sign, newSign);
	floodFill(image, i - 1, j + 1, rows, cols, sign, newSign);
	floodFill(image, i + 1, j - 1, rows, cols, sign, newSign);
	floodFill(image, i + 1, j + 1, rows, cols, sign, newSign);
}

// Build adjacency in a 2D map according to traversal,
// i.e. create the edges in the graph.
export function buildAdjacency(symbols: string[], inputSequences: any[]): any[] {
	let adjacency: any[] = [];
	for (let index = 0; index < symbols.length; index++) {
		adjacency.push(new Array(symbols.length).fill(0));
	}

	// Build up adjacency. Essentially treat all indices
	// as nodes in a graph and connect them with edges.
	const rows: number = inputSequences.length;
	for (let i = 0; i < rows; i++) {
		const cols: number = inputSequences[i].length;
		for (let j = 0; j < cols; j++) {
			const currentIdx: number = toFlatIndex(i, j, cols);
			switch (symbols[currentIdx]) {
				case '|':
					if (i != 0 || i != rows - 1) {
						adjacency[currentIdx][toFlatIndex(i - 1, j, cols)] = 1;
						adjacency[currentIdx][toFlatIndex(i + 1, j, cols)] = 1;
					}
					break;
				case '-':
					if (j != cols - 1 || j != 0) {
						adjacency[currentIdx][toFlatIndex(i, j - 1, cols)] = 1;
						adjacency[currentIdx][toFlatIndex(i, j + 1, cols)] = 1;
					}
					break;
				case 'L':
					if (i != 0 || j != cols - 1) {
						adjacency[currentIdx][toFlatIndex(i - 1, j, cols)] = 1;
						adjacency[currentIdx][toFlatIndex(i, j + 1, cols)] = 1;
					}
					break;
				case 'J':
					if (i != 0 || j != 0) {
						adjacency[currentIdx][toFlatIndex(i - 1, j, cols)] = 1;
						adjacency[currentIdx][toFlatIndex(i, j - 1, cols)] = 1;
					}
					break;
				case '7':
					if (j != 0 || i != rows - 1) {
						adjacency[currentIdx][toFlatIndex(i, j - 1, cols)] = 1;
						adjacency[currentIdx][toFlatIndex(i + 1, j, cols)] = 1;
					}
					break;
				case 'F':
					if (j != cols - 1 || i != rows - 1) {
						adjacency[currentIdx][toFlatIndex(i, j + 1, cols)] = 1;
						adjacency[currentIdx][toFlatIndex(i + 1, j, cols)] = 1;
					}
					break;
				default:
					break;
			}
		}
	}
	return adjacency;
}
