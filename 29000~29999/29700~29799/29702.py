"""
[29702: 이상한 호텔의 송이](https://www.acmicpc.net/problem/29702)

Tier: Silver 4 
Category: bitmask, math
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

def g(n):
  b = bin(n)[2:]
  
  ln = len(b)
  
  k = n - 2 ** (ln - 1) + 1
  
  p("%d%018d" % (ln, k))
  


def solve():
  n = ii()
  
  while n > 0:
    g(n)
    
    n //= 2
  
  


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()