"""
[25373: 벼락치기](https://www.acmicpc.net/problem/25373)

Tier: Bronze 2
Category: 구현
"""


def solution():
  n = int(input())

  s = 1
  e = 100000000000000000
  ans = e

  while s <= e:
    mid = (s + e) // 2

    t = sum([max(i, 0) for i in range(mid, mid - 7, -1)])

    if n > t:
      s = mid + 1
    else:
      ans = min(ans, mid)
      e = mid - 1

  return ans


if __name__ == '__main__':
  print(solution())
