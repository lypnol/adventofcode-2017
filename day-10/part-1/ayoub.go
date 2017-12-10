package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func reverse(a []int, m int, offset int) {
	n := len(a)
	for i := 0; i < m/2; i++ {
		tmp := a[(offset+i)%n]
		a[(offset+i)%n] = a[(offset+m-1-i)%n]
		a[(offset+m-1-i)%n] = tmp
	}
}

func run(s string) string {
	var lengths []int
	var list []int

	for _, c := range strings.Split(s, ",") {
		l, _ := strconv.ParseInt(c, 10, 32)
		lengths = append(lengths, int(l))
	}

	n := 256
	for i := 0; i < n; i++ {
		list = append(list, i)
	}

	cur := 0
	skip := 0
	for _, l := range lengths {
		reverse(list, l, cur)
		cur = (cur + l + skip) % n
		skip++
	}

	return fmt.Sprintf("%d", list[0]*list[1])
}

func main() {
	fmt.Println(run(os.Args[1]))
}
