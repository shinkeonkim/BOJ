"""
[25628: 햄버거 만들기](https://www.acmicpc.net/problem/25628)

Tier: Bronze 4
Category: 구현
"""


def solution():
  a, b = map(int, input().split())
  return min(a // 2, b)


if __name__ == '__main__':
  print(solution())
