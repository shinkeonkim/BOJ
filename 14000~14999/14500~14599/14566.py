"""
[14566: Donqiak N1](https://www.acmicpc.net/problem/14566)

Tier: Bronze 1
Category: 정렬
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
  n = ii()
  l = sorted(mii())
  
  dis = []
  
  for i in range(n - 1):
    dis.append(l[i+1] - l[i])
  
  mn = min(dis)
  p(mn, dis.count(mn))
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
