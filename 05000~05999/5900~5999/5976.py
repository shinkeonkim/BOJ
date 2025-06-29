"""
[5976: A spiral walk](https://www.acmicpc.net/problem/5976)

Tier: Silver 5 
Category: implementation
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
  sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda : [*map(int,inp().split())]
mfi = lambda : [*map(float,inp().split())]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
  n = ii()

  l = [[0] * n for _ in range(n)]

  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]

  x, y = 0, 0
  crt = 1
  d = 0

  while crt <= n * n:
    l[y][x] = crt
    crt += 1

    ny = y + dy[d]
    nx = x + dx[d]

    if nx < 0 or nx >= n or ny < 0 or ny >= n or l[ny][nx] != 0:
      d = (d + 1) % 4
      ny = y + dy[d]
      nx = x + dx[d]

    x, y = nx, ny

  for i in range(n):
    for j in range(n):
      print(l[i][j], end=" ")
    print()


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()