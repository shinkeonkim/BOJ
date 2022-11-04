"""
[25773: Number Maximization](https://www.acmicpc.net/problem/25773)

Tier: Bronze 2
Category: 정렬, 구현
"""


def solution():
  return ''.join(sorted([*input()], reverse=True))


if __name__ == '__main__':
  print(solution())
