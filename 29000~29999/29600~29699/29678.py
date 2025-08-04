"""
[29678: Монеты и гнезда](https://www.acmicpc.net/problem/29678)

Tier: Silver 4 
Category: greedy, sorting
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

  bring = mii()
  need = mii()

  l = [] # 몇개 있어야 한다. 결국 얻게되는 개수
  for i in range(n):
    l.append((need[i] - bring[i], bring[i]))

  l.sort(key=lambda x: (x[0], -x[1]))

  for i in range(n):
    minimum, gain = l[i]

    if minimum <= m:
      m += gain
  
  print(m)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
