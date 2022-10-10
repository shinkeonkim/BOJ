"""
[25305: 커트라인](https://www.acmicpc.net/problem/25305)

Tier: Bronze 2
Category: 구현
"""


def solution():
  n, k = map(int, input().split())
  scores = sorted([*map(int, input().split())], reverse=True)

  return scores[k - 1]


if __name__ == '__main__':
  print(solution())
