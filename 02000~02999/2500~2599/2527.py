"""
[2527: 직사각형](https://www.acmicpc.net/problem/2527)

Tier: Silver 1 
Category: case_work, geometry
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

def intersect_type(a, b):
  if a[0] > b[0]:
    a, b = b, a
  
  if a[1] < b[0]:
    return 0 # 안 겹침
  
  if a[1] == b[0]:
    return 1 # 점
  
  return 2


def solve():
  l = mii()
  A = l[:4]
  B = l[4:]
  
  x_type = intersect_type(
    [A[0], A[2]],
    [B[0], B[2]]
  )
  
  y_type = intersect_type(
    [A[1], A[3]],
    [B[1], B[3]]
  )
  
  if x_type == 0 or y_type == 0:
    return "d"
  
  if x_type == y_type == 1:
    return "c"
  
  if x_type == y_type == 2:
    return "a"
  
  return "b"


if __name__ == "__main__":
  tc = 4
  for t in range(1, tc+1):
    ret = solve()
    
    p(ret)