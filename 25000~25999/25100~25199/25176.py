"""
[25176: 청정수열 (Easy)](https://www.acmicpc.net/problem/25176)

Tier: Bronze 1
Category: 구현
"""


def solution(n):
  ans = 1

  for i in range(n):
    ans *= i + 1

  return ans


if __name__ == '__main__':
  print(solution(int(input())))
