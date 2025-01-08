"""
[16967: 배열 복원하기](https://www.acmicpc.net/problem/16967)

Tier: Silver 3 
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
  h, w, x, y = mii()
  l = [mii() for _ in range(h+x)]
  
  ans = [[0]*w for _ in range(h)]

  for i in range(h+x):
    for j in range(w+y):
      if i < h and j < w:
        if i < x or j < y:
          ans[i][j] = l[i][j]
        else:
          ans[i][j] = l[i][j] - ans[i-x][j-y]

  for i in range(h):
    print(*ans[i])

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()