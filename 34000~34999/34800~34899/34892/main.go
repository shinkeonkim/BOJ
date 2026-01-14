package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

func Print(a ...interface{}) {
	fmt.Fprintln(writer, a...)
}

func Solve() {
	var N, A, B, C, D, E, F, G, H int
	fmt.Fscan(reader, &N, &A, &B, &C, &D, &E, &F, &G, &H)

	cnt := 0
	ans := [3]int{}

loop:
	for x := 0; x <= N; x++ {
		for y := 0; y <= N-x; y++ {
			z := N - x - y

			if A*x+B*y+C*z == D && E*x+F*y+G*z == H {
				cnt++
				ans[0], ans[1], ans[2] = x, y, z
			}
		}

		if cnt > 1 {
			break loop
		}
	}

	switch cnt {
	case 0:
		Print(2)
	case 1:
		Print(0)
		Print(ans[0], ans[1], ans[2])
	default:
		Print(1)
	}
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	Solve()
}
