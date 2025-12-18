# [13035: Rectangle and Squares](https://www.acmicpc.net/problem/13035)
# Tier: Bronze 1
# Category: math, arithmetic

def solve
  a, b, c = gets.split.map(&:to_i)

  target_area = a * b
  ans = c * c
  k = target_area / (c * c)

  for i in [k - 10, 1].max..(k + 10)
    area = c * c * i

    if (area - target_area).abs < (ans - target_area).abs
      ans = area
    end
  end
  return ans
end

tc = gets.to_i
tc.times do |i|
  puts solve
end
