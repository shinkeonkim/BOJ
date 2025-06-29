"""
[11477: Lucky Chances](https://www.acmicpc.net/problem/11477)

Tier: Silver 5 
Category: bruteforcing, implementation
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

  ans = 0
  for i in range(n):
    for j in range(m):
      
      for k in range(0, i):
        if l[i][j] <= l[k][j]:
          break
      else:
        ans += 1
      
      for k in range(i + 1, n):
        if l[i][j] <= l[k][j]:
          break
      else:
        ans += 1

      for k in range(0, j):
        if l[i][j] <= l[i][k]:
          break
      else:
        ans += 1
      
      for k in range(j + 1, m):
        if l[i][j] <= l[i][k]:
          break
      else:
        ans += 1
  print(ans)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()