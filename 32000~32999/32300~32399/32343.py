"""
[32343: 드랍 더 비트](https://www.acmicpc.net/problem/32343)

Tier: Bronze 1 
Category: bitmask, bruteforcing, greedy
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
  a, b = mii()

  mx = 2 ** n - 1

  A = []
  B = []

  if a == 0:
    A.append(0)
  if b == 0:
    B.append(0)

  for i in range(mx + 1):
    k = bin(i)[2:]
    one_cnt = k.count('1')

    if one_cnt == a:
      A.append(i)
    if one_cnt == b:
      B.append(i)
  
  
  ans = 0
  for i in A:
    for j in B:
      ans = max(ans, i ^ j)
  
  p(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()

