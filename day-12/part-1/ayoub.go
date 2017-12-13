package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func bfs(graph [][]int, start int) map[int]bool {
	visited := make(map[int]bool)
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
	return visited
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

	visited := bfs(graph, 0)
	return fmt.Sprintf("%d", len(visited))
}

func main() {
	fmt.Println(run(os.Args[1]))
}
