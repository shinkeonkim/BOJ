"""
[28798: Старик и шахматная доска](https://www.acmicpc.net/problem/28798)

Tier: Bronze 1 
Category: math
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


def solve():
  n, m = mii()
  # n개의 흰색 칸, m개의 검은색 칸

  start = 0
  end = 10 ** 10

  ans = 0

  while start <= end:
    mid = (start + end) // 2
  
    # 체스판의 너비가 mid 일때

    if mid % 2 == 0:
      need = mid ** 2 // 2

      if need <= n and need <= m:
        ans = mid
        start = mid + 1
      else:
        end = mid - 1
    else:
      more = mid ** 2 // 2 + 1
      less = mid ** 2 // 2

      if (more <= n and less <= m) or (more <= m and less <= n):
        ans = mid
        start = mid + 1
      else:
        end = mid - 1
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
