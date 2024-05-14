"""
[22885: Reversort](https://www.acmicpc.net/problem/22885)

Tier: Bronze 1
Category: 정렬, 구현
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
  l = mii()
  ans = 0

  for i in range(n - 1):
    mn_idx = i
    for j in range(i + 1, n):
      if l[j] < l[mn_idx]:
        mn_idx = j
    
    ans += mn_idx - i + 1
    
    l = l[:i] + l[i:mn_idx+1][::-1] + l[mn_idx + 1:]
    
  p(ans)
  

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    p(end = f"Case #{t}: ")
    ret = solve()
