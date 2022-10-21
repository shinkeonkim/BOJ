"""
[25756: 방어율 무시 계산하기](https://www.acmicpc.net/problem/25756)

Tier: Bronze 3
Category: 구현
"""


def solution():
  n = int(input())
  l = [*map(int, input().split())]

  v = 0

  for i in l:
    v = 1 - (1 - v) * (1 - i / 100)

    print(v * 100)


if __name__ == '__main__':
  solution()
