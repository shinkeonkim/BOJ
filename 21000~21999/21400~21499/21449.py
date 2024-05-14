"""
[21449: Красивая таблица результатов](https://www.acmicpc.net/problem/21449)

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
  n, m = mii()
  l = mii()
  
  d = {}
  
  i = 1
  while i * i <= m:
    if m % i == 0:
      d[i] = 1
      d[m // i] = 1
    
    i+= 1
  
  cnt = 0
  for i in l:
    crt = i
  
    while d.get(crt + 1, False):
      crt += 1
      cnt += 1
  
  p(cnt)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
