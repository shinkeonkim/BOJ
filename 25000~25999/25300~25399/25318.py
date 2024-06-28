"""
[25318: solved.ac 2022](https://www.acmicpc.net/problem/25318)

Tier: Silver 1 
Category: implementation, string
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
  
  if n == 0:
    return 0


  l = [inp().split() for _ in range(n)]
  
  tms = []
  
  for a, b, tier in l:
    tier = int(tier)
    Y, M, D = map(int, a.split("/"))
    
    h, m, s = map(int, b.split(":"))
    
    tm = datetime(Y, M, D, h, m, s)
    
    tms.append([tm, tier])
  
  
  tms.sort(key = lambda t:t[0])

  weight = []
  
  
  last_t = tms[-1][0]
  for i in range(n):
    tm, tier = tms[i]
    weight.append(max((0.5) ** ((last_t - tm).days / 365), 0.9 ** (n - (i + 1))))
    
  down = sum(weight)
  
  up = 0
  for i in range(n):
    up += tms[i][1] * weight[i]
  
  # p(up, down, up / down)
  # p(weight)
  
  return up / down


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)