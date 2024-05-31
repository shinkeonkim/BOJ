"""
[20922: 겹치는 건 싫어](https://www.acmicpc.net/problem/20922)

Tier: Silver 1 
Category: two_pointer
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
  l = mii()
  
  cnt = {}
  
  start = 0
  cnt[l[0]] = 1
  
  ans = 1
  
  for i in range(1, n):
    cnt[l[i]] = cnt.get(l[i], 0) + 1
    
    while cnt[l[i]] > k:
      cnt[l[start]] -= 1
      start += 1
    
    ans = max(ans, i - start + 1)

  p(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()