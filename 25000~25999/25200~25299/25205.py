"""
[25205: 경로당펑크 2077](https://www.acmicpc.net/problem/25205)

Tier: Bronze 2
Category: 구현
"""


def solution():
  a = 'qwertasdfgzxcv'

  n = int(input())
  s = input()

  if s[-1] in a:
    return 1

  return 0


if __name__ == '__main__':
  print(solution())
