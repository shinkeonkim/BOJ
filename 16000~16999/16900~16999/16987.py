"""
[16987: 계란으로 계란치기](https://www.acmicpc.net/problem/16987)

Tier: Gold 5 
Category: backtracking, bruteforcing
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
  l = [mii() for _ in range(n)]

  def dfs(idx):
    if idx == n:
      cnt = 0
      for i in range(n):
        if l[i][0] <= 0:
          cnt += 1
      return cnt

    if l[idx][0] <= 0:
      return dfs(idx + 1)

    skip = 0
    max_cnt = 0
    for i in range(n):
      if i == idx or l[i][0] <= 0:
        skip += 1
        continue
      a = l[i][1]
      b = l[idx][1]
      l[idx][0] -= a
      l[i][0] -= b
      max_cnt = max(max_cnt, dfs(idx + 1))
      l[idx][0] += a
      l[i][0] += b

    if skip == n:
      max_cnt = max(max_cnt, dfs(idx + 1))

    return max_cnt

  p(dfs(0))

  
    

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()