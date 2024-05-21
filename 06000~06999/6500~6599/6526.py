"""
[6526: 모호한 순열](https://www.acmicpc.net/problem/6526)

Tier: Bronze 1
Category: 구현

그냥 인덱스를 저장하면 된다.
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
  while 1:
    n = ii()
    
    if n == 0:
      break
    
    l = mii()
    
    idx = [0] * n
    
    for i in range(n):
      idx[l[i] - 1] = i + 1
    
    for i in range(n):
      if idx[i] != l[i]:
        p(end="not ")
        break
    p("ambiguous")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
