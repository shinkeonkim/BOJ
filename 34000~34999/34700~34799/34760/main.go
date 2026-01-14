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

func ReadIntSlice(size int) []int {
	ret := make([]int, size)
	for i := 0; i < size; i++ {
		fmt.Fscan(reader, &ret[i])
	}
	return ret
}

func Solve() {
	ar := ReadIntSlice(15)
	mx := ar[0]
	mxIdx := 0
	mxCnt := 1
	for i := 1; i < 15; i++ {
		if ar[i] > mx {
			mx = ar[i]
			mxIdx = i
			mxCnt = 1
		} else if ar[i] == mx {
			mxCnt++
		}
	}

	if mxCnt == 1 && mxIdx == 14 {
		Print(mx)
	} else {
		Print(mx + 1)
	}

}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	Solve()
}
