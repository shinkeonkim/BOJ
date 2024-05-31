"""
[20529: 가장 가까운 세 사람의 심리적 거리](https://www.acmicpc.net/problem/20529)

Tier: Silver 1 
Category: bruteforcing, pigeonhole_principle
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

def dis(a, b):
  return sum(a[i] != b[i] for i in range(4))

def solve():
  n = ii()
  d = {}

  for s in inp().split():
    d[s] = d.get(s, 0) + 1
  
  mx = max(d.values())
  
  if mx >= 3:
    return 0
  
  l = [*d.keys()]
  k = len(l)
  ans = 100000
  
  for i in range(k):
    for j in range(i + 1, k):
      a = l[i]
      b = l[j]

      for last in range(k):
        c = l[last]
        
        if last == i and d[c] == 1:
          continue
        if last == j and d[c] == 1:
          continue

        crt = dis(a, b) + dis(b, c) + dis(a, c)
        
        ans = min(ans, crt)
  return ans

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    
    p(ret)