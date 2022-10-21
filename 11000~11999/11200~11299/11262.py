"""
[11262: Minions’ Master](https://www.acmicpc.net/problem/11262)

Tier: Bronze 2
Category: 구현
"""

import math


def round(value, decimals=0):
  multiplyWith = 10 ** decimals
  return math.floor(value * multiplyWith + 0.5) / multiplyWith


def solution():
  for _ in range(int(input())):
    n, *l = [*map(int, input().split())]
    s = sum(l)

    cnt = 0
    for i in l:
      if i * n > s:
        cnt += 1

    print("%.3f %.3f%%" % (round(s / n, 3), round(cnt / n * 100, 3)))


if __name__ == '__main__':
  solution()
