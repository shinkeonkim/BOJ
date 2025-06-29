"""
[29155: 개발자 지망생 구름이의 취업 뽀개기](https://www.acmicpc.net/problem/29155)

Tier: Silver 3 
Category: greedy, sorting
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

  problem = [0] + mii()

  l = [mii() for _ in range(n)]

  d = { 1: [], 2: [], 3: [], 4: [], 5: [] }

  for k, t in l:
    d[k].append(t)
  
  for k in d:
    d[k].sort()
  
  ans = -60

  for k in range(1, 6):
    if problem[k] == 0:
      continue
    
    ans += 60

    ans += d[k][0]

    for i in range(1, problem[k]):
      ans += 2 * d[k][i] - d[k][i-1] 

  p(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()