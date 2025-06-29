"""
[29263: Штурм](https://www.acmicpc.net/problem/29263)

Tier: Bronze 2 
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
  n, m = mii()

  l = [mii() for _ in range(n)]

  dy = [0, 1, 0, -1]
  dx = [1, 0, -1, 0]
  ans = 0
  for i in range(n):
    for j in range(m):
      chk = True
      for d in range(4):
        ni, nj = i + dy[d], j + dx[d]
        
        if ni < 0 or ni >= n or nj < 0 or nj >= m:
          continue
        
        if l[i][j] <= l[ni][nj]:
          chk = False
          break
      if chk:
        # print(i, j)
        ans += 1

  p(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()