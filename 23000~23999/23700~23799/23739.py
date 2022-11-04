"""
[23739: 벼락치기](https://www.acmicpc.net/problem/23739)

Tier: Bronze 1
Category: 구현
"""


def solution():
  n = int(input())
  l = [int(input()) for i in range(n)]
  ans = 0

  idx = 0
  for i in range(n):
    if idx >= n:
      break

    left_time = 30
    while left_time > 0:
      if idx >= n:
        break
      t = min(left_time, l[idx])

      if t * 2 >= l[idx]:
        ans += 1

      left_time -= t
      idx += 1

  return ans


if __name__ == '__main__':
  print(solution())
