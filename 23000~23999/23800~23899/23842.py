"""
[23842: 성냥개비](https://www.acmicpc.net/problem/23842)

Tier: Silver 4 
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
  l = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
  
  n = ii()
  
  # ab + cd = ef
  for a in range(10):
    for b in range(10):
      for c in range(10):
        for d in range(10):
          for e in range(10):
            for f in range(10):
              if a * 10 + b + c * 10 + d == e * 10 + f and l[a] + l[b] + l[c] + l[d] + l[e] + l[f] == n - 4:
                p(f"{a}{b}+{c}{d}={e}{f}")
                return
  
  p("impossible")
      

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()