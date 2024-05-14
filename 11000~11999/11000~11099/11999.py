"""
[11999: Milk Pails (Bronze)](https://www.acmicpc.net/problem/11999)

Tier: Silver 5
Category: 구현
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  x, y, m = mii()
  ans = 0

  for a in range(0, m // x + 1):
    left = m - a * x
    b = left // y
    
    ans = max(ans, a * x + b * y)

  p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
