"""
[4779: 칸토어 집합](https://www.acmicpc.net/problem/4779)

Tier: Silver 3 
Category: divide_and_conquer, recursion
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

ar = ["" for _ in range(13)]

def f(n):
  if ar[n] != "":
    return ar[n]
  
  ar[n] = f(n - 1) + " " * (3 ** (n-1)) + f(n - 1)
  
  return ar[n]

def solve():
  ar[0] = "-"
  
  while 1:
    try:
      n = ii()
    except:
      break
    
    p(f(n))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()