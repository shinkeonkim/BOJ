"""
[31800: Best Chance](https://www.acmicpc.net/problem/31800)

Tier: Bronze 1 
Category: implementation
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
  plus = mii()
  price = mii()
  
  l = [[i, plus[i], price[i]] for i in range(n)]
  
  l.sort(key = lambda t : -t[1])
  
  기회비용 = []
  
  기회비용.append(l[1][1] - l[0][2])
  
  for i in range(1, n):
    기회비용.append(l[0][1] - l[i][2])
  
  ans = [0] * n


  for i in range(n):
    ans[l[i][0]] = l[i][1] - 기회비용[i] - l[i][2]

  p(*ans)  
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()