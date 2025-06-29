"""
[15235: Olympiad Pizza](https://www.acmicpc.net/problem/15235)

Tier: Silver 5 
Category: data_structures, implementation, queue, simulation
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

  s = sum(l)
  idx = 0
  cnt = 0
  ans = {}

  while s > 0:
    if l[idx % n] > 0:
      cnt += 1
      l[idx % n] -= 1
      if l[idx % n] == 0:
        ans[idx % n] = cnt
      s -= 1
    idx += 1
    
  print(*[ans[i] for i in range(n)])




if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()