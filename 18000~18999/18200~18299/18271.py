"""
[18271: Preokret](https://www.acmicpc.net/problem/18271)

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
  n = ii()
  l = [ii() for _ in range(n)]

  final_score = [None, 0, 0]
  equal_score_count = 1
  max_reversion_length = 0


  final_score[l[0]] += 1

  for i in range(1, n):
    final_score[l[i]] += 1

    if final_score[1] == final_score[2]:
      equal_score_count += 1
    

  l2 = []

  current = l[0]
  cnt = 1

  for i in range(1, n):
    if l[i] == current:
      cnt += 1
    else:
      l2.append((current, cnt))
      current = l[i]
      cnt = 1
  l2.append((current, cnt))

  score = [0, 0, 0]

  for team, count in l2:
    if score[team] < score[3 - team] and score[team] + count > score[3 - team]:
      max_reversion_length = max(max_reversion_length, count)
    
    score[team] += count

  print(final_score[1], final_score[2])
  print(equal_score_count)
  print(max_reversion_length)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
