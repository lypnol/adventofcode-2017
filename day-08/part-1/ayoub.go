package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func eval(reg map[string]int64, name, inst string, val int64, cond []string) {
	var err error

	cond1 := int64(0)
	if cond1, err = strconv.ParseInt(cond[0], 10, 64); err != nil {
		cond1, _ = reg[cond[0]]
	}

	cond2 := int64(0)
	if cond2, err = strconv.ParseInt(cond[2], 10, 64); err != nil {
		cond2, _ = reg[cond[2]]
	}

	op := cond[1]

	if op == "<" && !(cond1 < cond2) {
		return
	} else if op == "<=" && !(cond1 <= cond2) {
		return
	} else if op == ">" && !(cond1 > cond2) {
		return
	} else if op == ">=" && !(cond1 >= cond2) {
		return
	} else if op == "==" && !(cond1 == cond2) {
		return
	} else if op == "!=" && !(cond1 != cond2) {
		return
	}

	current, _ := reg[name]

	if inst == "inc" {
		reg[name] = current + val
	} else if inst == "dec" {
		reg[name] = current - val
	}
}

func run(s string) string {
	reg := make(map[string]int64)
	for _, line := range strings.Split(s, "\n") {
		parts := strings.Split(line, " ")

		name := parts[0]
		inst := parts[1]
		val, _ := strconv.ParseInt(parts[2], 10, 64)
		cond := parts[4:]
		eval(reg, name, inst, val, cond)
	}

	max := int64(math.MinInt64)
	for _, v := range reg {
		if max < v {
			max = v
		}
	}

	return fmt.Sprintf("%d", max)
}

func main() {
	fmt.Println(run(os.Args[1]))
}
