"""
[1439: 뒤집기](https://www.acmicpc.net/problem/1439)

Tier: Silver 5
Category: 구현
"""


def solution():
  s = input()
  cnt = 1

  for i in range(1, len(s)):
    if s[i - 1] != s[i]:
      cnt += 1

  return cnt // 2


if __name__ == '__main__':
  print(solution())
