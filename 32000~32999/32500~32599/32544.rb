# [32544: Human Pyramid](https://www.acmicpc.net/problem/32544)
# Tier: Bronze 1
# Category: bruteforcing, math

n = gets.to_i

start = 0
ed = 1_000_000_000
ans = 0

while start < ed
  mid = (start + ed) / 2

  if mid * (mid + 1) / 2 <= n
    start = mid + 1
    ans = [ans, mid].max
  else
    ed = mid
  end
end
puts ans
