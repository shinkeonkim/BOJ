"""
[22061: Покупка велосипеда](https://www.acmicpc.net/problem/22061)

Tier: Bronze 2
Category: 구현
"""

import sys


def solution():
  for _ in range(int(input())):
    a, b, c = map(int, sys.stdin.readline().split())

    c -= min(b * 2, c - c % 2)

    if c <= a:
      print('YES')
    else:
      print('NO')


if __name__ == '__main__':
  solution()
