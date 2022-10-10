"""
[16120: PPAP](https://www.acmicpc.net/problem/16120)

Tier: Gold 4
Category: 스택
"""

s = input()

stk = []

for i in range(len(s)):
  stk.append(s[i])

  while len(stk) > 3:
    if stk[-1] == stk[-3] == stk[-4] == 'P' and stk[-2] == 'A':
      for _ in range(4):
        stk.pop()
      stk.append('P')
    else:
      break

if stk == ['P']:
  print('PPAP')
else:
  print('NP')
