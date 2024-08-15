"""
[14225: 부분수열의 합](https://www.acmicpc.net/problem/14225)

Tier: Silver 1 
Category: bruteforcing
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
  
  maked = set()
  
  for i in range(1 << (n + 1)):
    s = 0
    for j in range(n):
      if i & (1 << j):
        s += l[j]
    
    maked.add(s)
    
  
  start = 0
  
  l2 = sorted(list(maked))
    
  for i in l2:
    if start != i:
      p(start)
      return
    start += 1
  
  p(start)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()