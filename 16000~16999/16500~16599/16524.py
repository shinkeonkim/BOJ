"""
[16524: Database of Clients](https://www.acmicpc.net/problem/16524)

Tier: Silver 4 
Category: data_structures, hash_set, implementation, parsing, string, tree_set, set
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

def f(s):
  s = s.replace(".", "")
  
  if "+" in s:
    s = s.split("+")[0]
  
  return s


def solve():
  n = ii()
  l = [inp() for _ in range(n)]

  d = {}

  for i in l:
    a, b = i.split("@")

    if b not in d:
      d[b] = set()
    
    a = f(a)
    d[b].add(a)
  
  ans = 0
  for v in d.values():
    ans += len(v)
  
  p(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()