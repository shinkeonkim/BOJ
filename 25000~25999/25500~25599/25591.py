"""
[25591: 푸앙이와 종윤이](https://www.acmicpc.net/problem/25591)

Tier: Bronze 4
Category: 구현
"""


def solution():
  a, b = map(int, input().split())
  x = 100 - a
  y = 100 - b
  c = 100 - x - y
  d = x * y

  print(x, y, c, d, d // 100, d % 100)
  print(c + d // 100, d % 100)


if __name__ == '__main__':
  solution()
