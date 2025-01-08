"""
[11976: Promotion Counting](https://www.acmicpc.net/problem/11976)

Tier: Bronze 1 
Category: arithmetic, math
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
  l = [mii() for _ in range(4)]
  
  l = l[::-1]
  
  ans = []
  
  minus = 0
  
  for a, b in l:
    a -= minus
    minus = 0
    
    if a < b:
      minus = b - a
      ans.append(b - a)
    else:
      ans.append(0)
  
  print(*ans[::-1][1:], sep="\n")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()