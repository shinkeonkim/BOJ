"""
[31279: САМОЛЕТИ](https://www.acmicpc.net/problem/31279)

Tier: Bronze 2 
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
  N, D, ap1_d, ap2_d = mii()

  ap1_distance = 0
  ap2_distance = 0

  meet_count = 1
  # 두 비행기가 동일한 시점에 동일한 공항에 위치한 횟수 (이를 ‘만남’이라고 정의함). 초기 위치도 포함됩니다.

  cross_count = 0 # 두 비행기가 교차한 횟수 
  # (한 비행기가 어떤 공항을 비행 중에 다른 비행기가 그 공항에 착륙해 있는 경우). 단, 동시에 착륙한 경우는 포함하지 않습니다.
  
  ap1_check = [False] * N
  ap2_check = [False] * N

  ap1_pos = 0
  ap2_pos = 0

  ap1_check[ap1_pos] = True
  ap2_check[ap2_pos] = True

  for _ in range(N - 1):
    # 비행기 1 이동

    for i in range(ap1_d):
      ap1_pos += 1
      ap1_distance += 1
      ap1_pos %= N

      if ap2_pos == ap1_pos:
        cross_count += 1

    while ap1_check[(ap1_pos + 1) % N]:
      ap1_pos += 1
      ap1_distance += 1
      ap1_pos %= N
      
      if ap2_pos == ap1_pos:
        cross_count += 1
    ap1_pos = (ap1_pos + 1) % N
    ap1_distance += 1

    ap1_check[ap1_pos] = True

    if ap1_pos == ap2_pos:
      meet_count += 1
  
    # 비행기 2 이동

    for i in range(ap2_d):
      ap2_pos = (ap2_pos - 1 + N) % N
      ap2_distance += 1

      if ap1_pos == ap2_pos:
        cross_count += 1

    while ap2_check[(ap2_pos - 1 + N) % N]:
      ap2_pos = (ap2_pos - 1 + N) % N
      ap2_distance += 1

      if ap1_pos == ap2_pos:
        cross_count += 1

    ap2_pos = (ap2_pos - 1 + N) % N
    ap2_distance += 1
    ap2_check[ap2_pos] = True

    if ap1_pos == ap2_pos:
      meet_count += 1

  print(ap1_distance * D, ap2_distance * D, meet_count, cross_count)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
