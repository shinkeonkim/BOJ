"""
[32803: Ruffians](https://www.acmicpc.net/problem/32803)

Tier: Bronze 2 
Category: bruteforcing, implementation
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
  A = mii()
  B = mii()

  a = {}
  b = {}

  for idx, i in enumerate(A):
    a[i] = a.get(i, set())
    a[i].add(idx)
  
  for idx, i in enumerate(B):
    b[i] = b.get(i, set())
    b[i].add(idx)
  
  for i in A:
    x = a.get(i, set())
    y = b.get(i, set())

    flag = len(x - y) > 0 and len(y - x) > 0

    if (len(x) > 1 and len(y) > 0) or (len(y) > 1 and len(x) > 0):
      flag = True


    if flag:
      return "YES"
  return "NO"


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()

    print(ret)