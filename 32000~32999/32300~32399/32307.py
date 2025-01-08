"""
[32307: Injured Shoulder](https://www.acmicpc.net/problem/32307)

Tier: Bronze 2 
Category: data_structures, hash_set, implementation, string
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
  l = [inp() for _ in range(n)]
  
  m = ii()
  l2 = [inp() for _ in range(m)]
  
  s2 = set()
  
  for i in range(n):
    for j in range(i, n):
      s2.add(l[i] + l[j])
      s2.add(l[j] + l[i])
  
  for i in range(m):
    if l2[i] in l:
      p(1)
    elif l2[i] in s2:
      p(2)
    else:
      p(0)
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()