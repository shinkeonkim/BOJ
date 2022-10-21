"""
[25784: Easy-to-Solve Expressions ](https://www.acmicpc.net/problem/25784)

Tier: Bronze 5
Category: 구현
"""


def solution():
  a, b, c = map(int, input().split())

  if a + b == c or a + c == b or b + c == a:
    return 1

  if a * b == c or a * c == b or b * c == a:
    return 2

  return 3


if __name__ == '__main__':
  print(solution())
