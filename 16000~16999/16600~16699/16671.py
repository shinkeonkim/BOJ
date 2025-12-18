"""
[16671: Lazyland](https://www.acmicpc.net/problem/16671)

Tier: Silver 3 
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
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  n, k = mii()

  chosen_work = mii() # 선택한 일 번호
  persuade_time = mii() # 설득 시간

  d = defaultdict(list)
  for i in range(n):
    d[chosen_work[i]].append(persuade_time[i])
  
  need_work_count = k - len(d)

  surplus = []

  for times in d.values():
    if len(times) == 1:
      continue

    times.sort(reverse=True)
    surplus.extend(times[1:])
  
  surplus.sort()

  print(sum(surplus[:need_work_count]) if need_work_count > 0 else 0)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
