"""
[7453: 합이 0인 네 정수](https://www.acmicpc.net/problem/7453)

Tier: Gold 2 
Category: binary_search, mitm, sorting, two_pointer
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
  A = []
  B = []
  C = []
  D = []

  for _ in range(n):
    a, b, c, d = mii()
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
  
  d = {}
  
  for i in range(n):
    for j in range(n):
      num = A[i] + B[j]
      d[num] = d.get(num, 0) + 1
  
  ans = 0
  for i in range(n):
    for j in range(n):
      num = C[i] + D[j]
      
      ans += d.get(-num, 0)
  
  p(ans)
      


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()