"""
[5990: Barn Echoes](https://www.acmicpc.net/problem/5990)

Tier: Bronze 1
Category: 구현

문자열의 길이가 그렇게 길지 않으므로, 길이별로 접두사, 접미사를 각각 비교하면 된다.
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
  a = inp()
  b = inp()
  
  ans = 0
  
  for ln in range(1, len(a) + 1):
    x = a[:ln]
    y = b[-ln:]
    
    if x == y:
      ans = max(ans, ln)
    
  p(ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
