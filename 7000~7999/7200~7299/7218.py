"""
[7218: Pasislėpę romėniški skaičiai](https://www.acmicpc.net/problem/7218)

Tier: Bronze 3
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
  n = ii()
  s = inp()
  
  d = [
    ["I", 1], ["II", 2], ["III", 3], ["IV", 4], ["V", 5],
    ["VI", 6], ["VII", 7], ["VIII", 8], ["IX", 9], ["X", 10],
    ["XI", 11], ["XII", 12]
  ]
  
  ans = set()

  for i in range(n):
    for rom, num in d:
      if s[i:i+len(rom)] == rom:
        ans.add(num)
  
  ans = sorted(list(ans))
  
  p(*ans)


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
