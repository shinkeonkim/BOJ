"""
[33106: Problem C](https://www.acmicpc.net/problem/33106)

Tier: Bronze 1 
Category: implementation, string
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
  s = inp()
  ans = ""
  for idx, i in enumerate(s):
    if i == 'c':
      if idx == len(s) - 1 or (s[idx + 1] in 'aou') or (s[idx + 1] not in 'aeiou' and s[idx + 1] not in 'hy'):
        ans += "k"
      elif s[idx + 1] in 'eiy':
        ans += "s"
      else:
        ans += "c"
    else:
      if i == 'h' and idx > 0 and s[idx - 1] == 'c':
        continue
      ans += i
  
  print(ans)





if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()