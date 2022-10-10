"""
[2597: 줄자접기](https://www.acmicpc.net/problem/2597)

Tier: Silver 4
Category: 구현
"""


def solution():
  n = float(input())
  l = [sorted([*map(int, input().split())]) for i in range(3)]

  for i in range(3):
    if l[i][0] == l[i][1]:
      continue

    center = (l[i][1] + l[i][0]) / 2

    n = max(n - center, center)

    for j in range(i + 1, 3):
      for k in range(2):
        l[j][k] = abs(center - l[j][k])

  return n


if __name__ == '__main__':
  print(solution())
