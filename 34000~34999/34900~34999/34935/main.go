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

func ReadIntSlice(size int) []int {
	ret := make([]int, size)
	for i := 0; i < size; i++ {
		fmt.Fscan(reader, &ret[i])
	}
	return ret
}

func Solve() {
	n := ReadInt()
	ar := ReadIntSlice(n)

	for i := 0; i < n-1; i++ {
		if ar[i] < ar[i+1] {
			continue
		}
		Print(0)
		return
	}
	Print(1)
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	Solve()
}
