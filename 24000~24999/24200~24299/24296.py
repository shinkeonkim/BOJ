"""
[24296: ЛИНИЯ](https://www.acmicpc.net/problem/24296)

Tier: Bronze 3
Category: 구현
"""


def solution(n):
  if n % 2 == 0:
    return n

  return solution(n // 2 + 1)


if __name__ == '__main__':
  print(solution(int(input())))
