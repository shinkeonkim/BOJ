"""
[29072: Игра в перерыве](https://www.acmicpc.net/problem/29072)

Tier: Silver 2 
Category: data_structures, greedy, hash_set, priority_queue, sorting, set
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

import heapq

def solve():
  n = ii()
  l = mii()
  l.sort()

  pq = l[::]

  heapq.heapify(pq)
  ans = max(pq)

  while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)

    if a != b:
      heapq.heappush(pq, b)
    else:
      ans = max(ans, a + b)
      heapq.heappush(pq, a + b)

  p(ans)
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()