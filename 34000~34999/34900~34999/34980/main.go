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

func ReadInt() int {
	var n int
	fmt.Fscan(reader, &n)
	return n
}

func Solve() {
	n := ReadInt()
	var before, after string

	fmt.Fscan(reader, &before, &after)

	if before == after {
		Print("Good")
		return
	}

	beforeCnt := 0
	afterCnt := 0

	for i := 0; i < n; i++ {
		if before[i] == 'w' {
			beforeCnt++
		}

		if after[i] == 'w' {
			afterCnt++
		}
	}

	if beforeCnt == afterCnt {
		Print("Its fine")
	} else if beforeCnt < afterCnt {
		Print("Manners maketh man")
	} else {
		Print("Oryang")
	}
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	Solve()
}
