"""
[11544: D as Daedalus](https://www.acmicpc.net/problem/11544)

Tier: Bronze 1
Category: 구현
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  n, m = mii()

  org = 0
  mx = 0
  for _ in range(m):
    B, *l = mii()
    
    s = sum(l)
    if B >= s:
      org += l[0]
    
    crt = 0
    for i in [1, 10, 100, 1000, 10000]:
      if B >= s - l[0] + i:
        crt = i
    
    mx += crt
  
  p(mx - org)
    
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
