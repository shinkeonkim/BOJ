"""
[12871: 무한 문자열](https://www.acmicpc.net/problem/12871)

Tier: Silver 5
Category: 문자열
"""


def solution():
  a = input()
  b = input()

  a, b = len(b) * a, len(a) * b

  return 1 if a == b else 0


if __name__ == '__main__':
  print(solution())
