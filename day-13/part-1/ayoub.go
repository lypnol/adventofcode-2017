package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func run(s string) string {
	collisionHash := 0
	for _, line := range strings.Split(s, "\n") {
		parts := strings.Split(line, ": ")
		idx, _ := strconv.Atoi(parts[0])
		depth, _ := strconv.Atoi(parts[1])
		if idx%((depth-1)*2) == 0 {
			collisionHash += idx * depth
		}
	}

	return fmt.Sprintf("%d", collisionHash)
}

func main() {
	fmt.Println(run(os.Args[1]))
}
