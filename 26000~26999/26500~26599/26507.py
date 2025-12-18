"""
[26507: Rhonda](https://www.acmicpc.net/problem/26507)

Tier: Bronze 1 
Category: implementation, string
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
  n = ii()
  chips = []
  for _ in range(n):
    chip = [[*map(int, list(inp()))] for _ in range(10)]
    inp() # 빈줄 처리
    chips.append(chip)
  
  Q = ii()
  for _ in range(Q):
    query = mii()

    ans = [[0] * 10 for _ in range(10)]

    for idx in query:
      for i in range(10):
        for j in range(10):
          ans[i][j] += chips[idx][i][j]
    
    for i in range(10):
      for j in range(10):
        print(f"{ans[i][j]:02d}", end=" ")
      print()
    print()


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
