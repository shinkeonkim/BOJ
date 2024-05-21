"""
[3578: Holes](https://www.acmicpc.net/problem/3578)

Tier: Bronze3
Category: 구현
"""


def solution(n):
  if n <= 2:
    return [1, 0, 8][n]

  if n % 2 == 1:
    return '4' + '8' * (n // 2)

  return '8' * (n // 2)


if __name__ == '__main__':
  print(solution(int(input())))
