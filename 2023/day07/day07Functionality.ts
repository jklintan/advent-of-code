//**Helper functions for day 7 */

export function calculateBidTimesRanking(inputData: number[], bidData: number[], startRanking: number): number {
    let winningHands: number = 0;
    let ranking: number = startRanking;
    for (let i = 0; i < inputData.length; i++) {
        winningHands += bidData[inputData[i]] * ranking;
        ranking -= 1;
    }
    return winningHands;
}

export function sortData(handData: string[], playCards: string[], useJoker: boolean = false): any[] {
    let fiveOfAKind: number[] = [];
    let fourOfAKind: number[] = [];
    let fullHouse: number[] = [];
    let threeOfAKind: number[] = [];
    let twoPair: number[] = [];
    let onePair: number[] = [];
    let highCard: number[] = [];
    for (let i = 0; i < handData.length; i++) {
        const element: string = handData[i];
        let currentHand: number[] = Array(13).fill(0);
        for (let index = 0; index < element.length; index++) {
            const idx: number = playCards.indexOf(element[index]);
            currentHand[idx] += 1;
        }

        // Part 2, divide all hands which have a J in them to
        // be the type of the best possible hand that we can get.
        const numJs: number = currentHand[currentHand.length - 1];
        if (useJoker && numJs > 0) {
            if (numJs == 5) {
                fiveOfAKind.push(i);
            } else if (numJs == 4) {
                fiveOfAKind.push(i);
            } else if (numJs == 3) {
                if (currentHand.indexOf(2) >= 0) {
                    fiveOfAKind.push(i);
                } else {
                    fourOfAKind.push(i);
                }
            } else if (numJs == 2) {
                if (currentHand.indexOf(3) >= 0) {
                    fiveOfAKind.push(i);
                } else {
                    const numPairs: number = currentHand.filter(x => x === 2).length;
                    if (numPairs > 1) {
                        fourOfAKind.push(i);
                    } else {
                        threeOfAKind.push(i);
                    }
                }
            } else {
                if (currentHand.indexOf(4) >= 0) {
                    fiveOfAKind.push(i);
                } else if (currentHand.indexOf(3) >= 0) {
                    fourOfAKind.push(i);
                } else if (currentHand.indexOf(2) >= 0) {
                    const numPairs: number = currentHand.filter(x => x === 2).length;
                    if (numPairs == 2) {
                        fullHouse.push(i);
                    } else {
                        threeOfAKind.push(i);
                    }
                } else {
                    onePair.push(i);
                }
            }
        } else {
            if (currentHand.indexOf(5) >= 0) {
                fiveOfAKind.push(i);
            } else if (currentHand.indexOf(4) >= 0) {
                fourOfAKind.push(i);
            } else if (currentHand.indexOf(3) >= 0) {
                if (currentHand.indexOf(2) >= 0) {
                    fullHouse.push(i);
                } else {
                    threeOfAKind.push(i);
                }
            } else {
                const numPairs: number = currentHand.filter(x => x === 2).length;
                if (numPairs == 2) {
                    twoPair.push(i);
                } else if (numPairs == 1) {
                    onePair.push(i);
                } else {
                    highCard.push(i);
                }
            }
        }
    }
    return [fiveOfAKind, fourOfAKind, fullHouse, threeOfAKind, twoPair, onePair, highCard];
}

export function getTotalWinnings(types: any[], handData: string[], bidData: number[], playCards: string[]): number {
    let ranking: number = bidData.length;
    let winningHands: number = 0;
    for (let i = 0; i < types.length; i++) {
        types[i].sort(function (a: number, b: number) {
            const a1: string = handData[a];
            const a2: string = handData[b];

            for (let i = 0; i < a1.length; i++) {
                const id1: number = playCards.indexOf(a1[i]);
                const id2: number = playCards.indexOf(a2[i]);
                if (id1 < id2) return -1;
                if (id1 > id2) return 1;
            }
            return 0;
        });
        winningHands += calculateBidTimesRanking(types[i], bidData, ranking);
        ranking -= types[i].length;
    }
    return winningHands;
}
