//** Functionality for traversing the graph/map in day 08 of advent of code 2023. **/
import { Graph } from 'typescript-graph'

// Use a graph for easy access to nodes.
export type NodeType = { name: string, L: string, R: string };
export const graph = new Graph<NodeType>((n: NodeType) => n.name);

function getStartNodes(startString: string, nodeData: string[], inputGraph: Graph<NodeType>): NodeType[] {
    const nodes: string[] = nodeData.filter((x) => x.endsWith(startString));
    let allNodes: NodeType[] = [];
    for (let i = 0; i < nodes.length; i++) {
        const n: any = inputGraph.getNode(nodes[i]);
        if (n) { allNodes.push(n); }
    }

    return allNodes;
}

function findFirstTwoEndItems(endString: string, nodes: NodeType[], directions: string[], inputGraph: Graph<NodeType>): any[] {
    let endItems: any[] = [];
    for (let i = 0; i < nodes.length; i++) {
        endItems.push([]);
        let steps: number = 0;
        let directionIdx: number = 0;

        // Find the first occurence and then the next after
        // that to determine which loop count we have.
        while (endItems[i].length < 2) {
            const currentNode: any = nodes[i];
            let nextNode: any;
            if (directions[directionIdx] == "L") {
                nextNode = inputGraph.getNode(currentNode.L);
            } else {
                nextNode = inputGraph.getNode(currentNode.R);
            }

            if (nextNode) {
                nodes[i] = nextNode;
            }

            steps += 1;
            directionIdx += 1;
            if (directionIdx == directions.length) {
                directionIdx = 0;
            }

            if (nodes[i].name.endsWith(endString)) {
                endItems[i].push(steps);
            }
        }
    }
    return endItems;
}

// Gets the minimum number of steps when traversing
// the map from start to end, for one or many paths.
export function getStepsTraversingMap(startString: string, endString: string, nodeData: string[], inputGraph: Graph<NodeType>, directionsMap: string): number {
    // Get the start nodes.
    const directions: string[] = directionsMap.split("");
    const startNodes: NodeType[] = getStartNodes(startString, nodeData, inputGraph);

    // Find the first 2 occurences of end items for all start nodes.
    const endItems: any[] = findFirstTwoEndItems(endString, startNodes, directions, inputGraph);

    // Support for irregular starts and loops in case we
    // would reach the first Z sooner than the circle for
    // the loop, but our input is nice and is even.
    let loopStep: number[] = [];
    let startStep: number[] = [];
    for (let i = 0; i < endItems.length; i++) {
        startStep.push(endItems[i][0]);
        loopStep.push(endItems[i][1] - endItems[i][0]);
    }

    // Use the item with the maximum loop size, in order
    // to minimize as much as possible in terms of iterations.
    const loop: number = Math.max(...loopStep);
    const idx: number = startStep.indexOf(loop);
    let foundSolution: boolean = false;
    let circleStep: number = -1;
    while (!foundSolution) {
        const tryStep = startStep[idx] + circleStep * loop;
        foundSolution = true;
        circleStep += 1;
        for (let i = 0; i < startStep.length; i++) {
            if (i == idx) {
                continue;
            }
            const t: number = (tryStep - startStep[i]) / loopStep[i];
            if (!Number.isInteger(t) || t < 0) {
                foundSolution = false;
            }
        }
    }
    return startStep[idx] + circleStep * loop;
}
