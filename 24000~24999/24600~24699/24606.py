"""
[24606: Double Password](https://www.acmicpc.net/problem/24606)

Tier: Bronze 4
Category: 구현
"""


def solution():
  a = input()
  b = input()

  ans = 1
  for i in range(4):
    if a[i] != b[i]:
      ans *= 2

  return ans


if __name__ == '__main__':
  print(solution())
