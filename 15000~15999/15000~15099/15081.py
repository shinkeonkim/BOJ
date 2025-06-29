"""
[15081: Is Everybody Appy?](https://www.acmicpc.net/problem/15081)

Tier: Silver 5 
Category: bruteforcing, data_structures, hash_set, implementation, string, tree_set
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
  n = ii()
  d = {}
  ans = []
  for _ in range(n):
    k, *l = inp().split()
    k = int(k)

    for i in l:
      ret = d.get(i, False)

      if ret:
        continue

      d[i] = True
      ans.append(i)
      break
  
  print(*ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()