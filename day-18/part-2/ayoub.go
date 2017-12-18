package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"sync"
	"time"
)

func eval(reg map[byte]int64, v string) int64 {
	val, err := strconv.ParseInt(v, 10, 64)
	if err != nil {
		return reg[v[0]]
	}

	return val
}

var count int64
var isBlocked []bool
var locks sync.Mutex

func updateIsBlocked(id int, value bool) {
	locks.Lock()
	defer locks.Unlock()
	isBlocked[id] = value
}

func areBothBlocked() bool {
	locks.Lock()
	defer locks.Unlock()
	return isBlocked[0] && isBlocked[1]
}

func execute(instructions []string, id int, input chan int64, output chan int64) {
	defer updateIsBlocked(id, true)

	reg := make(map[byte]int64)
	reg['p'] = int64(id)
	offset := int64(0)
	n := int64(len(instructions))
	for offset < n && offset >= 0 {
		parts := strings.Split(instructions[offset], " ")
		if parts[0] == "set" {
			reg[parts[1][0]] = eval(reg, parts[2])
		} else if parts[0] == "add" {
			reg[parts[1][0]] += eval(reg, parts[2])
		} else if parts[0] == "mul" {
			reg[parts[1][0]] *= eval(reg, parts[2])
		} else if parts[0] == "mod" {
			reg[parts[1][0]] %= eval(reg, parts[2])
		} else if parts[0] == "jgz" {
			if eval(reg, parts[1]) > 0 {
				offset += eval(reg, parts[2])
				continue
			}
		} else if parts[0] == "snd" {
			if id == 1 {
				count++
			}
			output <- eval(reg, parts[1])
		} else if parts[0] == "rcv" {
			updateIsBlocked(id, true)
			reg[parts[1][0]] = <-input
			updateIsBlocked(id, false)
		}
		offset++
	}
}

func run(s string) string {
	var instructions []string

	for _, line := range strings.Split(s, "\n") {
		if len(strings.Split(line, " ")) <= 1 {
			continue
		}
		instructions = append(instructions, line)
	}

	input1 := make(chan int64, 1024*1024*10)
	input2 := make(chan int64, 1024*1024*10)

	isBlocked = append(isBlocked, false, false)

	ticker := time.NewTicker(time.Millisecond).C
	go execute(instructions, 0, input1, input2)
	go execute(instructions, 1, input2, input1)

	countTime := 0
	for countTime < 10 {
		for !areBothBlocked() {
			<-ticker
		}
		countTime++
		time.Sleep(10 * time.Millisecond)
	}

	return fmt.Sprintf("%d", count)
}

func main() {
	fmt.Println(run(os.Args[1]))
}
