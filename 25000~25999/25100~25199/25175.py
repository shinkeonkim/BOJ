"""
[25175: 두~~부 두부 두부](https://www.acmicpc.net/problem/25175)

Tier: Bronze 3
Category: 구현
"""


def solution():
  N, M, K = map(int, input().split())

  return (M + K - 4 + N * 100000) % N + 1


if __name__ == '__main__':
  print(solution())
