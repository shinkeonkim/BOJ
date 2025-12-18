# [10025: 게으른 백곰](https://www.acmicpc.net/problem/10025)
# Tier: Silver 3
# Category: prefix_sum, two_pointer, sliding_window

N, K = gets.split.map(&:to_i)
l = Array.new(N) { gets.split.map(&:to_i) }.sort_by { |x| x[1] }

left = 0
right = 0
ans = 0

current_sum = l[0][0]

while left <= right and right + 1 < N

  right += 1
  current_sum += l[right][0]

  while l[right][1] - l[left][1] > 2 * K
    current_sum -= l[left][0]
    left += 1
    next
  end

  ans = [ans, current_sum].max
end

puts ans
