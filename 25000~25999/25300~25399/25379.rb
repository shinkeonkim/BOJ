# [25379: 피하자](https://www.acmicpc.net/problem/25379)
# Tier: Silver 4
# Category: greedy

INF = 10**12

n = gets.to_i
l = gets.split.map(&:to_i).map { |i| i % 2 }
ans = INF

total_odd_cnt = l.count(1)
total_even_cnt = l.count(0)

# 홀수일 때, 짝수를 지나쳐야 하는 개수
cnt = 0
left_even_cnt = total_even_cnt

for i in 0..n
  if l[i] == 0
    left_even_cnt -= 1
  else
    cnt += left_even_cnt
  end
end

ans = [ans, cnt].min

cnt = 0
left_odd_cnt = total_odd_cnt

for i in 0..n
  if l[i] == 1
    left_odd_cnt -= 1
  else
    cnt += left_odd_cnt
  end
end

ans = [ans, cnt].min

puts ans
