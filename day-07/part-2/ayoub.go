package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func findRoot(graph map[string][]string) string {
	parent := make(map[string]string)

	for node, children := range graph {
		for _, child := range children {
			parent[child] = node
		}
	}

	for node := range graph {
		if _, ok := parent[node]; !ok {
			return node
		}
	}
	return ""
}

func recCalcTotalWeights(graph map[string][]string, weight map[string]int, root string, cache map[string]int) int {
	if val, exists := cache[root]; exists {
		return val
	}
	res := weight[root]
	for _, child := range graph[root] {
		cache[child] = recCalcTotalWeights(graph, weight, child, cache)
		res += cache[child]
	}
	cache[root] = res
	return cache[root]
}

func calcTotalWeights(graph map[string][]string, weight map[string]int, root string) map[string]int {
	res := make(map[string]int)
	for node := range graph {
		res[node] = recCalcTotalWeights(graph, weight, node, make(map[string]int))
	}
	return res
}

func isBalanced(graph map[string][]string, totalWeight map[string]int, root string) bool {
	last := -1
	for _, child := range graph[root] {
		if last == -1 {
			last = totalWeight[child]
		} else if last != totalWeight[child] {
			return false
		}
	}
	return true
}

func findCorrectedWeight(graph map[string][]string, weight map[string]int, totalWeight map[string]int, root string) int {
	if len(graph[root]) == 0 || isBalanced(graph, totalWeight, root) {
		return -1
	}

	// Look for the wrong weight
	wrongChild := ""
	wantedWeight := 0
	occurence := make(map[int]int)
	for _, child := range graph[root] {
		if _, exists := occurence[totalWeight[child]]; exists {
			occurence[totalWeight[child]]++
			wantedWeight = totalWeight[child]
		} else {
			occurence[totalWeight[child]] = 1
		}
	}
	for _, child := range graph[root] {
		if occurence[totalWeight[child]] == 1 {
			wrongChild = child
			break
		}
	}

	// If the wrong child subtree is not balanced then keep on searching
	if !isBalanced(graph, totalWeight, wrongChild) {
		return findCorrectedWeight(graph, weight, totalWeight, wrongChild)
	}

	// If there is a wrong weight found the return the corrected one
	diff := int(math.Abs(float64(totalWeight[wrongChild]) - float64(wantedWeight)))
	if weight[wrongChild] > diff {
		return weight[wrongChild] - diff
	}

	return weight[wrongChild] + diff
}

func run(s string) string {
	graph := make(map[string][]string)
	weight := make(map[string]int)
	for _, line := range strings.Split(s, "\n") {
		parts := strings.Split(line, " ")
		w, _ := strconv.ParseInt(parts[1][1:len(parts[1])-1], 10, 32)
		weight[parts[0]] = int(w)
		if len(parts) == 2 {
			graph[parts[0]] = []string{}
		} else {
			graph[parts[0]] = append(graph[parts[0]], strings.Split(strings.Join(parts[3:], ""), ",")...)
		}
	}

	root := findRoot(graph)
	totalWeight := calcTotalWeights(graph, weight, root)
	answer := findCorrectedWeight(graph, weight, totalWeight, root)

	return fmt.Sprint(answer)
}

func main() {
	fmt.Println(run(os.Args[1]))
}
