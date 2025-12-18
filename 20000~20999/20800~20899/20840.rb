# [20840: Volleybollmatchen](https://www.acmicpc.net/problem/20840)
# Tier: Bronze 1
# Category: implementation, simulation

n = gets.to_i
s = gets.chomp

game_set_score = [0, 0]
current_set_score = [0, 0]
current_set = 0
minimum_score = [25, 25, 15]

s.each_char do |c|
  if c == 'A'
    winner = 0
    current_set_score[0] += 1
  else
    winner = 1
    current_set_score[1] += 1
  end

  if current_set_score[winner] >= minimum_score[current_set] and (current_set_score[0] - current_set_score[1]).abs >= 2
    game_set_score[winner] += 1
    current_set += 1
    current_set_score = [0, 0]
  end
end

puts "#{game_set_score[0]} #{game_set_score[1]}"
