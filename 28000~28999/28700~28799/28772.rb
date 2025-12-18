# [28772: Подсчет хештегов](https://www.acmicpc.net/problem/28772)
# Tier: Bronze 1
# Category: implementation, data_structures, string, set, hash_set, parsing

s = gets.chomp.split
h = Hash.new(0)
s.each { |word|  h[word] += 1 if word.start_with?("#") and word[1..] !~ /#/ and word.length > 1 }

puts h.size
h.each do |word, count|
  puts "#{word} #{count}"
end
