"""
[20953: 고고학자 예린](https://www.acmicpc.net/problem/20953)

Tier: Bronze 2
Category: 구현
"""

import sys


def solution():
  for tc in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    n = a + b

    print(n * n * (n - 1) // 2)


if __name__ == '__main__':
  solution()
