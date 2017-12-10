package main

import (
	"fmt"
	"os"
)

func reverse(a []int, m int, offset int) {
	n := len(a)
	for i := 0; i < m/2; i++ {
		tmp := a[(offset+i)%n]
		a[(offset+i)%n] = a[(offset+m-1-i)%n]
		a[(offset+m-1-i)%n] = tmp
	}
}

func hash(list, inputs []int, cur, skip int) (int, int) {
	n := len(list)
	for _, l := range inputs {
		reverse(list, l, cur)
		cur = (cur + l + skip) % n
		skip++
	}
	return cur, skip
}

func densify(list []int) []int {
	var res []int
	n := len(list)
	for i := 0; i < n/16; i++ {
		xor := 0
		for j := i * 16; j < i*16+16; j++ {
			xor = xor ^ list[j]
		}
		res = append(res, xor)
	}
	return res
}

func run(s string) string {
	var inputs []int
	var list []int

	for _, c := range s {
		inputs = append(inputs, int(c))
	}
	inputs = append(inputs, 17, 31, 73, 47, 23)

	n := 256
	for i := 0; i < n; i++ {
		list = append(list, i)
	}

	round := 0
	cur, skip := 0, 0
	for round < 64 {
		cur, skip = hash(list, inputs, cur, skip)
		round++
	}

	dense := densify(list)

	hex := ""
	for _, d := range dense {
		hex += fmt.Sprintf("%02x", d)
	}

	return hex
}

func main() {
	fmt.Println(run(os.Args[1]))
}
