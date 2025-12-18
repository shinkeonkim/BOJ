def is_good_word(word):
  stk = []

  for ch in word:
    if stk and stk[-1] == ch:
      stk.pop()
    else:
      stk.append(ch)

  return not stk

words = [input() for _ in range(int(input()))]
print(sum([1 for word in words if is_good_word(word)]))
