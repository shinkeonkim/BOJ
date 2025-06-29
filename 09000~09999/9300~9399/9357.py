"""
[9357: Eligibility](https://www.acmicpc.net/problem/9357)

Tier: Silver 4 
Category: data_structures, string, set, hash_set, tree_set
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
  n = ii()
  l = [inp() for _ in range(n)]

  d = {}

  for s in l:
    year = int(s.split()[-1])
    name = s[:-4]
    if name not in d:
      d[name] = set()
    d[name].add(year)
  
  ans = []

  for k, v in d.items():
    if len(v) < 5:
      ans.append(k)
  
  ans.sort()

  return ans


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()

    print(f"Case #{t}: ")
    print(*ret, sep="\n")