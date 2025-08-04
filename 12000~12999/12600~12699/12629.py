"""
[12629: Crazy Rows (Small)](https://www.acmicpc.net/problem/12629)

Tier: Silver 3 
Category: bruteforcing, implementation, sorting
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
  n = int(input())
  l = [[*map(int, list(input()))] for _ in range(n)]

  l2 = []
  for idx in range(n):
    i = l[idx]
    last_one_idx = -1

    for j in range(n):
      if i[j] == 1:
        last_one_idx = j
    
    l2.append(last_one_idx)
  
  ans = 0

  for i in range(n):
    target = -1
    for j in range(i, n):
      if l2[j] <= i:
        target = j
        break
    ans += target - i
    while target > i:
      l2[target], l2[target - 1] = l2[target - 1], l2[target]
      target -= 1

  return ans

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
    print(f"Case #{t}: {ret}")
