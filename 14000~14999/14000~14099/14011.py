"""
[14011: Small PhD Restaurant](https://www.acmicpc.net/problem/14011)

Tier: Silver 3 
Category: greedy, sorting
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
  n, balance = mii()
  a = mii()
  b = mii()
  
  l = [[a[i], b[i]] for i in range(n)]
  
  l.sort(key=lambda t : (t[0], -t[1]))
  
  for price, benefit in l:
    if price >= benefit:
      continue
    
    if price > balance:
      continue
    
    balance += benefit - price

  p(balance)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()