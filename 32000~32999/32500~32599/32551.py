"""
[32551: Composed Rhythms](https://www.acmicpc.net/problem/32551)

Tier: Bronze 2 
Category: ad_hoc, constructive, math
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
  
  cnt = -1
  for i in range(n):
    k = n - i * 2
    
    if k % 3 == 0:
      cnt = i
      break
  
  three_cnt = (n - 2 * cnt) // 3
  
  print(cnt + three_cnt)
  print(*[2] * cnt, *[3] * three_cnt)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()