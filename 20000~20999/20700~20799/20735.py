"""
[20735: Fifty Shades of Pink](https://www.acmicpc.net/problem/20735)

Tier: Bronze 2
Category: 구현
"""


def solution():
  cnt = 0

  for i in range(int(input())):
    s = input().lower()

    if 'pink' in s or 'rose' in s:
      cnt += 1

  return cnt if cnt > 0 else 'I must watch Star Wars with my daughter'


if __name__ == '__main__':
  print(solution())
