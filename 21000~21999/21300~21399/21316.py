"""
[21316: 스피카](https://www.acmicpc.net/problem/21316)

Tier: Silver 3 
Category: graphs, ad_hoc
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
  l = [mii() for _ in range(12)]
  count = [0] * 13

  for a, b in l:
    count[a] += 1
    count[b] += 1
  
  first_candidates = []

  for i in range(1, 13):
    if count[i] == 3:
      first_candidates.append(i)

  check = []

  for candidate in first_candidates:
    temp = []

    for i in range(12):
      if l[i][0] == candidate:
        temp.append(count[l[i][1]])
      elif l[i][1] == candidate:
        temp.append(count[l[i][0]])
    
    check.append([candidate] + sorted(temp))
  
  for i in range(len(check)):
    if check[i][1:] == [1, 2, 3]:
      print(check[i][0])

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
