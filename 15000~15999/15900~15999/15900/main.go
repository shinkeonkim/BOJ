package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

var depth [550000]int
var edges [550000][]int

func Print(a ...interface{}) {
	fmt.Fprintln(writer, a...)
}

func ReadInt() int {
	var n int
	fmt.Fscan(reader, &n)
	return n
}

func f(crt int, parent int) {
	for _, next := range edges[crt] {
		if next == parent {
			continue
		}
		depth[next] = depth[crt] + 1
		f(next, crt)
	}
}

func Solve() {
	n := ReadInt()

	for i := 0; i < n-1; i++ {
		var a, b int
		fmt.Fscan(reader, &a, &b)
		edges[a] = append(edges[a], b)
		edges[b] = append(edges[b], a)
	}

	for i := 1; i <= n; i++ {
		depth[i] = -1
	}

	depth[1] = 0
	f(1, -1)

	ans := 0

	for i := 1; i <= n; i++ {
		if len(edges[i]) != 1 {
			continue
		}

		ans += depth[i]
		ans %= 2
	}

	if ans == 1 {
		Print("Yes")
	} else {
		Print("No")
	}
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	Solve()
}
