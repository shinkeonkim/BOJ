package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

func Print(a ...interface{}) {
	fmt.Fprintln(writer, a...)
}

func Solve() {

	var w, h, r int
	fmt.Fscan(reader, &w, &h, &r)

	area := math.Pi * float64(r) * float64(r) / 4.0

	Print(float64(w)*float64(h) - area)
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	Solve()
}
