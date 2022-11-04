"""
[21918: 전구](https://www.acmicpc.net/problem/21918)

Tier: Bronze 2
Category: 구현
"""


def solution():
  n, m = map(int, input().split())
  l = [*map(int, input().split())]

  for i in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
      l[b - 1] = c
    if a == 2:
      for j in range(b - 1, c):
        l[j] = 1 - l[j]
    if a == 3:
      for j in range(b - 1, c):
        l[j] = 0
    if a == 4:
      for j in range(b - 1, c):
        l[j] = 1

  print(*l)


if __name__ == '__main__':
  solution()
