"""
[29934: Important Messages](https://www.acmicpc.net/problem/29934)

Tier: Silver 5 
Category: data_structures, hash_set, set
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
  l = set([inp() for _ in range(n)])
  m = ii()
  l2 = [inp() for _ in range(m)]

  ans = 0
  for s in l2:
    if s in l:
      ans += 1
  
  p(ans)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()