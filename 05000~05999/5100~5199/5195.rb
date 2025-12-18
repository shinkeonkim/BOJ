# [5195: Stump Speech](https://www.acmicpc.net/problem/5195)
# Tier: Bronze 1
# Category: implementation, string

def solve
  n = gets.to_i

  l = []

  n.times do
    word = gets.chomp
    score = gets.to_i

    l << [word, score]
  end

  total = 0
  sentence = gets.chomp

  l.each do |word, score|
    counting = 0
    for i in 0...(sentence.length - word.length + 1)
      counting += 1 if sentence[i...(i + word.length)] == word
    end
    total += score * counting
    # puts ([word, counting, score * counting])
  end

  total
end

tc = gets.to_i

for t in 1..tc
  ret = solve()

  puts "Data Set #{t}:\n#{ret}"
end
