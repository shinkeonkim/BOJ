"""
[29587: Последовательность](https://www.acmicpc.net/problem/29587)

Tier: Bronze 2 
Category: ad_hoc
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
  l = mii()
  
  d = [1] * n
  track = [-1] * n
  
  for i in range(n):
    for j in range(i):
      if l[j] >= l[i]:
        if d[i] < d[j] + 1:
          d[i] = d[j] + 1
          track[i] = j
  
  if max(d) == 1:
    p(0)
    return

  crt = d.index(max(d))
  ans = []
    
  while track[crt] != -1:
    ans.append(crt + 1)
    crt = track[crt]
  
  ans.append(crt + 1)
  
  ans.reverse()
  
  p(len(ans))
  p(*ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()