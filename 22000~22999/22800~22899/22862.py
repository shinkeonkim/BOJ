"""
[22862: 가장 긴 짝수 연속한 부분 수열 (large)](https://www.acmicpc.net/problem/22862)

Tier: Gold 5 
Category: two_pointer
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
from fractions import Fraction

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
  l = mii()
  
  even_groups = []
  odd_groups = []
  start = 0
  
  for i in range(n):
    if l[i] % 2 == 0:
      start = i
      break
  
  end=n - 1
  for i in range(n-1, -1, -1):
    if l[i] % 2 == 0:
      end = i
      break
  
  l = l[start:end+1]
  n = len(l)

  odd_cnt = 0
  even_cnt = 0
  
  for i in l:
    if i % 2 == 0:
      if odd_cnt > 0:
        odd_groups.append(odd_cnt)
        odd_cnt = 0
      even_cnt += 1
    else:
      if even_cnt > 0:
        even_groups.append(even_cnt)
        even_cnt = 0
      odd_cnt += 1
  if odd_cnt > 0:
    odd_groups.append(odd_cnt)
  if even_cnt > 0:
    even_groups.append(even_cnt)
    
  if len(even_groups) == 0:
    print(0)
    return
  
  assert(len(even_groups) == len(odd_groups) + 1)
  # print(even_groups)
  # print(odd_groups)

  start = 0
  end = 0
  odd_sum = 0
  ans = 0
  even_sum = even_groups[0]
  while start < len(even_groups) and end < len(even_groups):
    while odd_sum > k:
      odd_sum -= odd_groups[start]
      even_sum -= even_groups[start]
      start += 1
    ans = max(ans, even_sum)
    
    end += 1
    if end == len(even_groups):
      break
    even_sum += even_groups[end]
    odd_sum += odd_groups[end-1]
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
