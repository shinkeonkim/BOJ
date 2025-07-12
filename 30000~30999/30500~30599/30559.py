"""
[30559: Boat Commuter](https://www.acmicpc.net/problem/30559)

Tier: Bronze 1 
Category: implementation, simulation
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
  n, m , k = mii()
  l = [mii() for _ in range(k)]

  costs_by_card = defaultdict(lambda: 0)
  last_places = defaultdict(lambda: 0)

  for place, card in l:
    last_place = last_places[card]

    if last_place == 0:
      last_places[card] = place
    else:
      if last_place == place:
        costs_by_card[card] += 100
      else:
        costs_by_card[card] += abs(place - last_place)
      last_places[card] = 0
  
  for k, v in last_places.items():
    if v != 0:
      costs_by_card[k] += 100
  
  for i in range(1, m + 1):
    print(costs_by_card[i], end=' ')


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
