"""
[11923: PUTOVANJE](https://www.acmicpc.net/problem/11923)

Tier: Bronze 1 
Category: bruteforcing, implementation
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
  n, C = mii()
  weights = mii()

  ans = 0

  for start in range(0, n):
    cnt = 0
    crt = C

    if crt < weights[start]:
      continue
    
    for i in range(start, n):
      if crt < weights[i]:
        continue
      crt -= weights[i]
      cnt += 1
    ans = max(ans, cnt)
  
  print(ans)



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()