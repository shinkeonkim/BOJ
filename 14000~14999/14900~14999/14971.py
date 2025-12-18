"""
[14971: A Garden with Ponds](https://www.acmicpc.net/problem/14971)

Tier: Silver 3 
Category: bruteforcing, implementation
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
from functools import reduce, lru_cache
from operator import itemgetter, attrgetter, mul, add, sub, truediv
from typing import List, Tuple, Dict, Set, Any, Union

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


def solve(n, m):
  l = [mii() for _ in range(n)]
  ans = 0

  for i in range(n):
    for j in range(m):
      for d in range(2, n - i):
        for d2 in range(2, m - j):
          mn_height = float('inf')

          mn_height = min(mn_height, min(l[i][j:j + d2 + 1]))
          mn_height = min(mn_height, min(l[i + d][j:j + d2 + 1]))
          for k in range(1, d):
            mn_height = min(mn_height, l[i + k][j])
            mn_height = min(mn_height, l[i + k][j + d2])


          mx_height = float('-inf')

          mx_height = max(mx_height, max(l[i + 1][j + 1:j + d2]))
          mx_height = max(mx_height, max(l[i + d - 1][j + 1:j + d2]))
          for k in range(2, d - 1):
            mx_height = max(mx_height, l[i + k][j + 1])
            mx_height = max(mx_height, l[i + k][j + d2 - 1])

          if mn_height <= mx_height:
            continue
          
          ret = 0
          for y in range(i + 1, i + d):
            for x in range(j + 1, j + d2):
              ret += (mn_height - l[y][x])
          
          ans = max(ans, ret)
  return ans
            

if __name__ == "__main__":
  while 1:
    n, m = mii()
    if n == m == 0:
      break

    print(solve(n, m))