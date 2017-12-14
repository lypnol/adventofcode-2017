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

func countRegions(grid [][]bool, totalUsed int) int {
	count := 0
	visited := make(map[int]bool)
	for len(visited) < totalUsed {
		start := -1
		for i := range grid {
			for j := range grid {
				if !grid[i][j] {
					continue
				}
				if _, isVisited := visited[i*128+j]; !isVisited {
					start = i*128 + j
					break
				}
			}
			if start != -1 {
				break
			}
		}

		var queue []int
		queue = append(queue, start)
		for len(queue) > 0 {
			current := queue[0]
			i, j := current/128, current%128
			queue = queue[1:]
			visited[current] = true
			for _, u := range []int{-1, 0, 1} {
				for _, v := range []int{-1, 0, 1} {
					if !((u == 0 && v != 0) || (u != 0 && v == 0)) {
						continue
					}
					x, y := i+u, j+v
					if !(x >= 0 && x < 128 && y >= 0 && y < 128) {
						continue
					}
					if !grid[x][y] {
						continue
					}
					if _, isVisited := visited[x*128+y]; !isVisited {
						queue = append(queue, x*128+y)
					}
				}
			}
		}
		count++
	}

	return count
}

func run(s string) string {
	var grid [][]bool

	totalUsed := 0
	for i := 0; i < 128; i++ {
		grid = append(grid, []bool{})
		for j := 0; j < 128; j++ {
			grid[i] = append(grid[i], false)
		}

		rowKey := s + "-" + fmt.Sprintf("%d", i)
		hash := knothash(rowKey)
		for k, b := range hash {
			for j, p := range fmt.Sprintf("%.8b", b) {
				grid[i][j+k*8] = p == '1'
				if p == '1' {
					totalUsed++
				}
			}
		}
	}

	return fmt.Sprintf("%d", countRegions(grid, totalUsed))
}

func main() {
	fmt.Println(run(os.Args[1]))
}
