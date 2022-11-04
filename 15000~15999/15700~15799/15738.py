"""
[15738: 뒤집기](https://www.acmicpc.net/problem/15738)

Tier: Bronze 1
Category: 수학, 구현
"""


def solution():
  n, k, m = map(int, input().split())
  input()
  k -= 1

  t = [int(input()) for i in range(m)]

  for i in t:
    if i < 0:
      i += n
      if i <= k:
        k = n - (k - i + 1)
    else:
      i -= 1
      if k <= i:
        k = i - k

  return k + 1


if __name__ == '__main__':
  print(solution())
