"""
[6508: 구슬로 하는 게임](https://www.acmicpc.net/problem/6508)

Tier: Bronze 1
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
  while 1:
    n = ii()
    
    if n == 0:
      break
    
    l = mii()
    
    ans = 0
    
    added = 0
    
    for i in range(n - 1, -1, -1):
      ans += l[i] + added
      added += l[i] + added
    p(ans)
    
    

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
