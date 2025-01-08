"""
[7466: Honey and Milk Land](https://www.acmicpc.net/problem/7466)

Tier: Bronze 1 
Category: geometry, math, pythagoras
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
  a, b = mii()
  
  l = []
  while len(l) < a + b - 2:
    s = inp()      
    l.extend([*map(int, s.split())])

  A = l[:a - 1]
  B = l[a - 1:]

  if a == 1 and b == 1:
    print(0)
    return
  
  if a == 1:
    print(sum(B))
    return

  if b == 1:
    print(sum(A))
    return
  
  
  ans = 1
  sum_a = sum(A)
  sum_b = sum(B)
  
  while ans * ans < sum_a ** 2 + sum_b ** 2:
    ans += 1
  
  print(ans)
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()