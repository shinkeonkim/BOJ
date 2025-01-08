"""
[32316: Ready for Contest](https://www.acmicpc.net/problem/32316)

Tier: Bronze 1 
Category: implementation
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
  n, m = mii()
  
  l = [mii() for _ in range(m)]
  
  d = {}
  for i in range(1, n + 1):
    d[i] = set()
    
  for a, b in l:
    d[a].add(b)

  for i in range(1, n + 1):
    if 1 in d[i] and 2 in d[i]:
      print(i)
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
