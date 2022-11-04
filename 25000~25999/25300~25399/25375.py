"""
[25375: 아주 간단한 문제](https://www.acmicpc.net/problem/25375)

Tier: Silver 5
Category: 구현, 수학
"""


import sys


def solution():
  for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    if b % a == 0 and b // a > 1:
      print(1)
    else:
      print(0)


if __name__ == '__main__':
  solution()
