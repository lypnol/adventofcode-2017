package main

import (
	"fmt"
	"os"
	"strconv"
)

func run(s string) string {
	step, _ := strconv.Atoi(s)
	buffer := make([]int, 1, 2018)
	buffer[0] = 0
	curr := 0
	for i := 1; i < 2018; i++ {
		n := len(buffer)
		curr = (curr + step) % n
		buffer = append(buffer, 0)
		copy(buffer[curr+1:], buffer[curr:])
		buffer[curr+1] = i
		curr++
		if i == 2017 {
			return fmt.Sprintf("%d", buffer[(curr+1)%n])
		}
	}
	return ""
}

func main() {
	fmt.Println(run(os.Args[1]))
}
