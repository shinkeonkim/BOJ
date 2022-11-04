"""
[10408: The return of the King](https://www.acmicpc.net/problem/10408)

Tier: Bronze 1
Category: 구현
"""


def solution(s):
  l = []

  i = 0
  while i < len(s):
    if int(s[i]) > 1:
      l.append(int(s[i]))
    else:
      if i + 1 < len(s) and s[i + 1] == '0':
        l.append(10)
        i += 1
      else:
        l.append(1)
    i += 1

  return sum(l) / len(l)


if __name__ == '__main__':
  print('%.2f' % solution(input()))
