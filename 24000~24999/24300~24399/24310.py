"""
[24310: БОЯДИСВАНЕ НА ОГРАДА](https://www.acmicpc.net/problem/24310)

Tier: Bronze 3
Category: 구현
"""


def solution():
  a, b, c, d = map(int, input().split())

  a, b = min(a, b), max(a, b)
  c, d = min(c, d), max(c, d)

  if c < a:
    a, b, c, d = c, d, a, b

  s = (b - a + 1) + (d - c + 1)

  if c < b:
    s -= (min(d, b) - c + 1)

  return s


if __name__ == '__main__':
  print(solution())
