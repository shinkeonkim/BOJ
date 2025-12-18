"""
[33989: 벚꽃과 단풍](https://www.acmicpc.net/problem/33989)

Tier: Silver 3 
Category: dp, bruteforcing, prefix_sum
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
  n = int(input())
  s = input()

  total_b_count = s.count('B')

  b_count = 0
  d_count = 0

  ans = float('inf')

  if total_b_count == 0 or total_b_count == n:
    print(0)
    return
  
  ans = min(ans, total_b_count)
  ans = min(ans, n - total_b_count)

  for i in range(n):
    if s[i] == 'B':
      b_count += 1
    else:
      d_count += 1

    left_b_count = total_b_count - b_count
    ans = min(ans, left_b_count + d_count)

  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
