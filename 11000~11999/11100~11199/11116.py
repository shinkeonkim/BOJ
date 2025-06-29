"""
[11116: 교통량](https://www.acmicpc.net/problem/11116)

Tier: Silver 5 
Category: implementation, bruteforcing
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

  left = mii()
  right = mii()

  left_d = {}
  right_d = {}
  ans = 0

  for i in left:
    left_d[i] = left_d.get(i, 0) + 1
  for i in right:
    right_d[i] = right_d.get(i, 0) + 1
  
  for i in left_d:
    if left_d[i] <= 0:
      continue
    
    if left_d.get(i + 500, 0) > 0 and right_d.get(i + 1000, 0) > 0 and right_d.get(i + 1500, 0) > 0:
      left_d[i + 500] -= 1
      right_d[i + 1000] -= 1
      right_d[i + 1500] -= 1
      left_d[i] -= 1
      ans += 1
  
  print(ans)

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()