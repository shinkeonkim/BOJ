"""
[25640: MBTI](https://www.acmicpc.net/problem/25640)

Tier: Bronze 4
Category: 구현
"""


def solution():
  ans = 0
  s = input()

  for _ in range(int(input())):
    if s == input():
      ans += 1

  return ans


if __name__ == '__main__':
  print(solution())
