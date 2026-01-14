package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

func readLine() string {
	line, _, _ := reader.ReadLine()
	return string(line)
}

func readInt() int {
	var n int
	fmt.Fscan(reader, &n)
	return n
}

func readIntSlice(size int) []int {
	ret := make([]int, size)
	for i := 0; i < size; i++ {
		fmt.Fscan(reader, &ret[i])
	}
	return ret
}

func print(a ...interface{}) {
	fmt.Fprintln(writer, a...)
}

func solve() {
	a := readLine()
	b := readLine()

	a_x := int(a[0]) - 97
	a_y := int(a[1]) - 49

	b_x := int(b[0]) - 97
	b_y := int(b[1]) - 49

	x_diff := math.Abs(float64(a_x - b_x))
	y_diff := math.Abs(float64(a_y - b_y))

	if int(x_diff+y_diff)%2 == 0 {
		print("YES")
	} else {
		print("NO")
	}
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	solve()
}
