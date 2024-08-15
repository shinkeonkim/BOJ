"""
[6236: 용돈 관리](https://www.acmicpc.net/problem/6236)

Tier: Silver 2 
Category: binary_search, parametric_search
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
  N, K = mii()
  
  price = [ii() for _ in range(N)]
  
  left = max(price)
  right = sum(price)
  
  while left < right:
    mid = (left + right) // 2
    cnt = 1
    money = mid
    
    for p in price:
      if money < p:
        cnt += 1
        money = mid
      money -= p
    if cnt <= K:
      right = mid
    else:
      left = mid + 1
  
  print(left)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()