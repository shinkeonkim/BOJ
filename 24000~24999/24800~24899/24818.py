"""
[24818: Field Trip](https://www.acmicpc.net/problem/24818)

Tier: Bronze 1 
Category: arithmetic, implementation, math, prefix_sum
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

  if s % 3 :
    p(-1)
    return
  
  cnt = 0
  crt = 0
  ans = []
  for idx in range(n):
    i = l[idx]
    crt += i
    
    if crt * 3 == s:
      cnt += 1
      crt = 0
      ans.append(idx + 1)
  
  if cnt == 3 and crt == 0:
    p(*ans[:2])
  else:
    p(-1)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()