"""
[9468: Islands in the Data Stream](https://www.acmicpc.net/problem/9468)

Tier: Silver 5 
Category: ad_hoc, bruteforcing, implementation
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
  tc_num, *l = mii()

  stk = []
  cnt = 0

  for i in l:
    if len(stk) == 0:
      stk.append(i)
    else:
      if i == stk[-1]:
        continue
      elif stk[-1] > i:
        stk.pop()
        cnt += 1
      else:
        stk.append(i)
  p(f"{tc_num} {cnt}") 


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()