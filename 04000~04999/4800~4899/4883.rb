# [4883: 삼각 그래프](https://www.acmicpc.net/problem/4883)
# Tier: Silver 1
# Category: dp

tc = 0
INF = 10**9

while true
  tc += 1
  n = gets.to_i

  break if n == 0

  l = Array.new(n) { gets.split.map(&:to_i) }
  DP = Array.new(n) { Array.new(3, 0) }

  DP[0][0] = INF
  DP[0][1] = l[0][1] # 출발점
  DP[0][2] = l[0][1] + l[0][2]

  for i in 1...n
    DP[i][0] = [DP[i - 1][0], DP[i - 1][1]] .min + l[i][0]
    DP[i][1] = [DP[i][0], DP[i - 1][0], DP[i - 1][1], DP[i - 1][2]].min + l[i][1]
    DP[i][2] = [DP[i][1], DP[i - 1][1], DP[i - 1][2]].min + l[i][2]
  end

  puts "#{tc}. #{DP[n - 1][1]}"
end
