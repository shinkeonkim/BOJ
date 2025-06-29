"""
[8117: Triangles](https://www.acmicpc.net/problem/8117)

Tier: Silver 5 
Category: greedy, bruteforcing, sorting, geometry
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
  l = []

  while 1:
    a = ii()

    if a == 0:
      break
    
    l.append(a)
  
  l.sort()

  for i in range(len(l) - 2):
    for j in range(i + 1, len(l) - 1):
      for k in range(j + 1, len(l)):
        if l[i] + l[j] > l[k]:
          p(f"{l[i]} {l[j]} {l[k]}")
          return
  
  p("NIE")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()