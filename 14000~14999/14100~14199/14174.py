"""
[14174: Block Game](https://www.acmicpc.net/problem/14174)

Tier: Bronze 1 
Category: string
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


def get_cnt(s: str) -> dict:
  d = {}
  for i in s:
    d[i] = d.get(i, 0) + 1

  return d


def merge(a: dict, b: dict) -> dict:
  ret = a
  
  for k, v in b.items():
    ret[k] = max(ret.get(k, 0), v)
  
  return ret

def solve():
  n = ii()
  ans = [0] * 26  

  for _ in range(n):
    a, b = isplit()

    d1 = get_cnt(a)
    d2 = get_cnt(b)
    
    merged = merge(d1, d2)

    for k, v in merged.items():
      ans[ord(k) - 97] += v
    
  for i in ans:
    p(i)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
