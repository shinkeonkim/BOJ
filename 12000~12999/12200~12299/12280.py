"""
[12280: Sorting (Small)](https://www.acmicpc.net/problem/12280)

Tier: Silver 5 
Category: implementation, sorting
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

  even_idx = []
  odd_idx = []
  even = []
  odd = []

  for i in range(n):
    if l[i] % 2 == 0:
      even.append(l[i])
      even_idx.append(i)
    else:
      odd.append(l[i])
      odd_idx.append(i)
  
  even.sort(reverse=True)
  odd.sort()

  for i in range(len(even_idx)):
    l[even_idx[i]] = even[i]
  
  for i in range(len(odd_idx)):
    l[odd_idx[i]] = odd[i]
  
  return l


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    print("Case #{}: {}".format(t, " ".join(map(str, ret))))