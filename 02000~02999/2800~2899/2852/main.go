package main

import (
	"bufio"
	"fmt"
	"os"
)

var writer *bufio.Writer
var reader *bufio.Reader

func print(a ...interface{}) {
	fmt.Fprintln(writer, a...)
}

func mm_ss_to_int(time string) int {
	minute := int(time[0]-'0')*10 + int(time[1]-'0')
	second := int(time[3]-'0')*10 + int(time[4]-'0')

	return minute*60 + second
}

func int_to_mm_ss(time int) string {
	minute := time / 60
	second := time % 60

	return fmt.Sprintf("%02d:%02d", minute, second)
}

func readInt() int {
	var n int
	fmt.Fscanf(reader, "%d\n", &n)
	return n
}

func solve() {
	n := readInt()

	goal_team_numbers := make([]int, n)
	goal_times := make([]string, n+1) // 마지막 골은 실제 골이 아니라, 경기 종료 시간

	goal_influence_time := make([]int, n)
	influence_time := make([]int, 2)

	for i := 0; i < n; i++ {
		fmt.Fscanf(reader, "%d %s\n", &goal_team_numbers[i], &goal_times[i])
		goal_team_numbers[i]--
	}

	goal_times[n] = "48:00"

	for i := 0; i < n; i++ {
		goal_influence_time[i] = mm_ss_to_int(goal_times[i+1]) - mm_ss_to_int(goal_times[i])
	}

	score := [2]int{0, 0}

	for i := 0; i < n; i++ {
		team := goal_team_numbers[i]

		score[team]++

		if score[team] > score[1-team] {
			influence_time[team] += goal_influence_time[i]
		} else if score[team] < score[1-team] {
			influence_time[1-team] += goal_influence_time[i]
		}
	}

	print(int_to_mm_ss(influence_time[0]))
	print(int_to_mm_ss(influence_time[1]))
}

func main() {
	writer = bufio.NewWriter(os.Stdout)
	reader = bufio.NewReader(os.Stdin)
	defer writer.Flush()

	solve()
}
