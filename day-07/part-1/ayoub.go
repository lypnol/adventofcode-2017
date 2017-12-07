package main

import (
	"fmt"
	"os"
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

func run(s string) string {
	graph := make(map[string][]string)
	for _, line := range strings.Split(s, "\n") {
		parts := strings.Split(line, " ")
		if len(parts) == 2 {
			graph[parts[0]] = []string{}
		} else {
			graph[parts[0]] = append(graph[parts[0]], strings.Split(strings.Join(parts[3:], ""), ",")...)
		}
	}
	return findRoot(graph)
}

func main() {
	fmt.Println(run(os.Args[1]))
}
