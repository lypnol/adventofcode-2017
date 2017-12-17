package main

import (
	"fmt"
	"os"
	"strconv"
)

func run(s string) string {
	step, _ := strconv.Atoi(s)
	curr := 0
	n := 1
	pos0 := 0
	after0 := -1
	for i := 1; i <= 50000000; i++ {
		curr = (curr + step) % n
		n++
		if curr < pos0 {
			pos0 = (pos0 + 1) % n
		}
		curr++
		if curr == (pos0+1)%n {
			after0 = i
		}
	}
	return fmt.Sprintf("%d", after0)
}

func main() {
	fmt.Println(run(os.Args[1]))
}
