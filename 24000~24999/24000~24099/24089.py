"""
[24089: ボールの移動 (Moving Balls)](https://www.acmicpc.net/problem/24089)

Tier: Bronze 2
Category: 구현
"""


def solution():
  d = {}
  N, M = map(int, input().split())

  for i in range(1, N + 1):
    d[i] = i

  for _ in range(M):
    a, b = map(int, input().split())

    d[a] = b

  for i in range(1, N + 1):
    print(d[i])


if __name__ == '__main__':
  solution()
