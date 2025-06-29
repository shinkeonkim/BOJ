"""
[2371: 파일 구별하기](https://www.acmicpc.net/problem/2371)

Tier: Silver 3 
Category: implementation, data_structures, bruteforcing, set, hash_set
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
  l = []

  mx_len = 0
  for _ in range(n):
    l.append(mii()[:-1])
    mx_len = max(mx_len, len(l[-1]))
  
  for i in range(0, mx_len):
    s = set()

    for j in range(n):
      s.add(tuple(l[j][:i+1]))
    
    if len(s) == n:
      print(i + 1)
      return


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()