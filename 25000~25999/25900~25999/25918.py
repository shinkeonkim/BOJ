"""
[25918: 북극곰은 괄호를 찢어](https://www.acmicpc.net/problem/25918)

Tier: Silver 1 
Category: ad_hoc, data_structures, greedy, stack
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
  s = inp()
  stk = []
  
  ans = 1
  
  for i in s:
    if len(stk) == 0:
      stk.append(i)      
      continue
    
    if i != stk[-1]:
      stk.pop()
    else:
      stk.append(i)
    
    ans = max(ans, len(stk))
  
  if len(stk) > 0:
    p(-1)
  else:
    p(ans)
      
      
      
    


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()