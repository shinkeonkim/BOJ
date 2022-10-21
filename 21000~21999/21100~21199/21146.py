"""
[21146: Rating Problems ](https://www.acmicpc.net/problem/21146)

Tier: Bronze 3
Category: 구현
"""


def solution():
  n, k = map(int, input().split())
  s = sum([int(input()) for _ in range(k)])

  print(f'{(s - 3 * (n-k)) / n} {(s + 3 * (n-k)) / n}')


if __name__ == '__main__':
  solution()
