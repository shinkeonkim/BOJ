"""
[25286: 11월 11일](https://www.acmicpc.net/problem/25286)

Tier: Bronze 3
Category: 구현
"""

from datetime import date, timedelta


def solution():
  for _ in range(int(input())):
    y, m = map(int, input().split())
    d = date(y, m, m) - timedelta(days=m)
    print(d.year, d.month, d.day)


if __name__ == '__main__':
  solution()
