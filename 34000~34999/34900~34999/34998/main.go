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

func ReadStringSlice(size int) []string {
	ret := make([]string, size)
	for i := 0; i < size; i++ {
		fmt.Fscan(reader, &ret[i])
	}
	return ret
}

func Solve() {
	k := ReadInt()
	s := ReadStringSlice(k*2 + 1)

	ans := 0

	for i := 0; i < 2*k+1; i += 2 {
		if s[i] == "!" {
			ans = -1
			break
		}

		ans += int(s[i][0] - '0')
	}

	if ans > 9 {
		ans = -1
	}

	if ans == -1 {
		Print("!")
		return
	}

	Print(ans)
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	tc := ReadInt()
	for i := 0; i < tc; i++ {
		Solve()
	}
}
