"""
[30282: Paskaitos](https://www.acmicpc.net/problem/30282)

Tier: Bronze 2 
Category: implementation
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

def to_number(h, m):
  return h * 60 + m

def is_intersection(a, b):
  if a[0] != b[0]:
    return False
  
  class_time = [
    (to_number(a[1], a[2]), to_number(a[3], a[4])),
    (to_number(b[1], b[2]), to_number(b[3], b[4]))
  ]
  
  class_time.sort()

  if class_time[0][1] <= class_time[1][0]:
    return False
  
  return True

def solve():
  time_table = [mii() for _ in range(10)]

  for i in range(10):
    for j in range(i + 1, 10):
      if is_intersection(time_table[i], time_table[j]):
        print("NE")
        print(i + 1, j + 1)
        return

  print("TAIP")

  ans = 0
  for i in range(10):
    ans += to_number(time_table[i][3], time_table[i][4]) - to_number(time_table[i][1], time_table[i][2])
  print(ans // 60, ans % 60)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
