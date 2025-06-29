"""
[33646: Pencil Crayons](https://www.acmicpc.net/problem/33646)

Tier: Bronze 1 
Category: greedy, implementation
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
  n, k = mii()

  l = [isplit() for _ in range(n)]

  ans = 0
  for i in l:
    d = {}
    for j in i:
      d[j] = d.get(j, 0) + 1
    
    for k, v in d.items():
      if v > 1:
        ans += v - 1
        break
  
  print(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()