package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func countSubGraphs(graph [][]int) int {
	visited := make(map[int]bool)
	count := 0
	for len(visited) != len(graph) {
		start := 0
		for x := range graph {
			if _, isVisited := visited[x]; !isVisited {
				start = x
				break
			}
		}
		queue := []int{}
		queue = append(queue, start)

		for len(queue) != 0 {
			current := queue[0]
			queue = queue[1:]
			visited[current] = true
			for _, child := range graph[current] {
				if _, isVisited := visited[child]; !isVisited {
					queue = append(queue, child)
				}
			}
		}
		count++
	}

	return count
}

func run(s string) string {
	var graph [][]int
	for _, line := range strings.Split(s, "\n") {
		splitted := strings.Split(line, " <-> ")
		x, _ := strconv.Atoi(splitted[0])
		graph = append(graph, []int{})
		for _, c := range strings.Split(splitted[1], ", ") {
			y, _ := strconv.Atoi(c)
			graph[x] = append(graph[x], y)
		}
	}

	count := countSubGraphs(graph)
	return fmt.Sprintf("%d", count)
}

func main() {
	fmt.Println(run(os.Args[1]))
}
