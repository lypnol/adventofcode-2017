package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func run(s string) string {
	for x := 0; ; x++ {
		caught := false
		for _, line := range strings.Split(s, "\n") {
			parts := strings.Split(line, ": ")
			idx, _ := strconv.Atoi(parts[0])
			depth, _ := strconv.Atoi(parts[1])
			if (idx+x)%((depth-1)*2) == 0 {
				caught = true
				break
			}
		}
		if !caught {
			return fmt.Sprintf("%d", x)
		}
	}
}

func main() {
	fmt.Println(run(os.Args[1]))
}
