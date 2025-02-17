"""
[29378: Гарри Поттер и нос Волан-де-Морта](https://www.acmicpc.net/problem/29378)

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
  n, m = mii()
  l = [inp() for _ in range(n)]

  ans = 0

  for i in range(n):
    for j in range(m):
      if l[i][j] == '.':
        if i + 1 < n and l[i+1][j] == '.':
          ans += 1
        if j + 1 < m and l[i][j+1] == '.':
          ans += 1
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()