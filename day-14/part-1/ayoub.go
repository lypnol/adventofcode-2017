package main

import (
	"fmt"
	"os"
)

func reverse(a []byte, m int, offset int) {
	n := len(a)
	for i := 0; i < m/2; i++ {
		tmp := a[(offset+i)%n]
		a[(offset+i)%n] = a[(offset+m-1-i)%n]
		a[(offset+m-1-i)%n] = tmp
	}
}

func knothash(input string) []byte {
	var res []byte
	var list []byte

	input += fmt.Sprintf("%c%c%c%c%c", 17, 31, 73, 47, 23)

	n := 256
	for i := 0; i < n; i++ {
		list = append(list, byte(i))
	}

	round := 0
	cur, skip := 0, 0
	for round < 64 {
		for _, l := range input {
			reverse(list, int(l), cur)
			cur = (cur + int(l) + skip) % n
			skip++
		}
		round++
	}

	for i := 0; i < n/16; i++ {
		xor := byte(0)
		for j := i * 16; j < i*16+16; j++ {
			xor = xor ^ list[j]
		}
		res = append(res, xor)
	}
	return res
}

func run(s string) string {
	count := 0
	for i := 0; i < 128; i++ {
		rowKey := s + "-" + fmt.Sprintf("%d", i)
		hash := knothash(rowKey)
		for _, b := range hash {
			for b > 0 {
				count += int(b & 1)
				b >>= 1
			}
		}
	}

	return fmt.Sprintf("%d", int(count))
}

func main() {
	fmt.Println(run(os.Args[1]))
}
