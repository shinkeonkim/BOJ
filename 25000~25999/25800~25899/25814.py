"""
[25814: Heavy Numbers](https://www.acmicpc.net/problem/25814)

Tier: Bronze 3
Category: 구현
"""


def weight(s):
  return len(s) * sum([*map(int, list(s))])


def solution():
  a, b = input().split()
  a = weight(a)
  b = weight(b)

  if a > b:
    return 1

  if a < b:
    return 2

  return 0


if __name__ == '__main__':
  print(solution())
