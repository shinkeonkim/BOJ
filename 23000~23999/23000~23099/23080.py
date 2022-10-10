"""
[23080: 스키테일 암호](https://www.acmicpc.net/problem/23080)

Tier: Bronze 3
Category: 구현
"""


def solution():
  k = int(input())
  return input()[0::k]


if __name__ == '__main__':
  print(solution())
