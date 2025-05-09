"""
[32158: SWAPC](https://www.acmicpc.net/problem/32158)

Tier: Bronze 1 
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
  s = list(inp())
  
  P = []
  C = []
  
  for i in range(n):
    if s[i] == 'P':
      P.append(i)
    elif s[i] == 'C':
      C.append(i)
  
  for i in range(min(len(P), len(C))):
    s[P[i]], s[C[i]] = s[C[i]], s[P[i]]
  
  print("".join(s))
  
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()