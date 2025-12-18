# [32351: 리듬게임](https://www.acmicpc.net/problem/32351)
# Tier: Bronze 1
# Category: math, implementation, arithmetic

def get_second(bpm, duration)
  60.0 / bpm * 4 * duration
end

def solve
  n,s_0,k = gets.split
  n = n.to_i
  s_0 = s_0.to_f
  k = k.to_i

  l = []

  prev_tm = 1

  k.times do
    a, b = gets.split
    a = a.to_i
    b = b.to_f
    l << [a, b]
  end

  l << [n + 1, 0]

  total_time = 0
  current_bpm = s_0

  l.each do |a, b|
    duration = a - prev_tm

    total_time += get_second(current_bpm, duration)
    # puts get_second(current_bpm, duration)
    prev_tm = a
    current_bpm = b
  end

  total_time
end

tc = 1
# tc = gets.to_i
tc.times do |i|
  # puts "Case ##{i + 1}: #{solve}"
  puts "%.12f" % solve
end
