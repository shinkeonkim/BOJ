"""
[4335: 숫자 맞추기](https://www.acmicpc.net/problem/4335)

Tier: Bronze 1
Category: 구현
"""


def solution():
  s = 1
  e = 10
  chk = True

  while 1:
    n = int(input())

    if n == 0:
      break

    str = input()

    if str == 'right on':
      if not s <= n <= e:
        chk = False
      print('Stan may be honest' if chk else 'Stan is dishonest')
      s = 1
      e = 10
      chk = True
    elif str == 'too high':
      if n <= s:
        chk = False
      e = min(e, n - 1)
    else:
      if e <= n:
        chk = False
      s = max(s, n + 1)


if __name__ == '__main__':
  solution()
