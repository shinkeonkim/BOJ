"""
[21207: Train Boarding](https://www.acmicpc.net/problem/21207)

Tier: Bronze 1 
Category: bruteforcing, case_work, implementation, math
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
  N, L, P = mii()

  cnt = [0] * N
  max_distance = 0
  people = [ii() for _ in range(P)]

  entrances = []

  for i in range(N):
    entrances.append(L * i + L // 2)
  
  for idx in range(P):
    person = people[idx]

    min_distance = float('inf')
    min_idx = -1

    for i in range(N):
      distance = abs(entrances[i] - person)

      if distance <= min_distance:
        min_distance = distance
        min_idx = i

    cnt[min_idx] += 1
    max_distance = max(max_distance, min_distance)
  
  print(max_distance)
  print(max(cnt))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
