"""
[14246: K보다 큰 구간](https://www.acmicpc.net/problem/14246)

Tier: Silver 3
Category: 구현
"""


def solution():
  n = int(input())
  l = [*map(int, input().split())] + [0]
  k = int(input())

  i = 0
  j = 1
  s = l[0]
  ans = 0

  while i < n and j <= n:
    if s > k:
      ans += n - j + 1
      s -= l[i]
      i += 1
    else:
      s += l[j]
      j += 1

  return ans


if __name__ == '__main__':
  print(solution())
