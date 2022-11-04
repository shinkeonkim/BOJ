"""
[25193: 곰곰이의 식단 관리](https://www.acmicpc.net/problem/25193)

Tier: Silver 5
Category: 구현, 그리디
"""


def solution():
  n = int(input())
  s = input()
  c = s.count('C')
  a = n - c + 1

  return c // a + (1 if c % a else 0)


if __name__ == '__main__':
  print(solution())
