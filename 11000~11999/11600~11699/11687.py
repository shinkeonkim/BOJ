"""
[11687: 팩토리얼 0의 개수](https://www.acmicpc.net/problem/11687)

Tier: Silver 1 
Category: binary_search, math, number_theory
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

def get_five_cnt(num):
  cnt = 0
  k = 5
  while num >= k:
    cnt += num // k
    k *= 5
  
  return cnt
    

def solve():
  n = ii()
  INF = 1000 * n
  left = 1
  right = INF
  ans = right

  while left <= right:
    mid = (left + right) // 2
    cnt = get_five_cnt(mid)
    
    if cnt > n:
      right = mid - 1
    elif cnt == n:
      ans = min(ans, mid)
      right = mid - 1
    else:
      left = mid + 1
  
  p(ans if ans != INF else -1)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()