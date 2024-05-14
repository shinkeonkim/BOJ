"""
[27964: 콰트로치즈피자](https://www.acmicpc.net/problem/27964)

Tier: Silver 5
Category: 문자열, 구현
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
  n = ii()
  l = set(inp().split())
  
  p("yummy" if sum([1 for i in l if i[-6:] == "Cheese"]) >= 4 else "sad")
    

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
