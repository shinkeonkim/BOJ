"""
[26587: Reverse](https://www.acmicpc.net/problem/26587)

Tier: Silver 5 
Category: implementation, string
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = False
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
  while True:
    try:
      s = inp().split()

      idxs = []

      for i in range(len(s)):
        if s[i][0] in "aeiouAEIOU":
          idxs.append(i)
      
      for i in range(len(idxs) // 2):
        s[idxs[i]], s[idxs[-i-1]] = s[idxs[-i-1]], s[idxs[i]]
      print(*s)
    except EOFError:
      break


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()