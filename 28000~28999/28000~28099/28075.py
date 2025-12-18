"""
[28075: 스파이](https://www.acmicpc.net/problem/28075)

Tier: Silver 3 
Category: implementation, bruteforcing, recursion
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
  n, m = mii()
  ans = [[[0] * (m + 1) for _ in range(3)] for _ in range(n)]
  
  l = [mii() for _ in range(2)] # 2 x 3
  
  # ans[i][j][k] # i번째 날에, j번째 작업을 했을때, k를 성취한 경우의 수
  
  for i in range(3):
    ans[0][i][min(l[0][i], m)] += 1
    ans[0][i][min(l[1][i], m)] += 1
  
  for i in range(1, n):
    # 같은 장소에서는 l 상에 주어진 것의 절반임
    for prev_place in range(3):
      for curr_place in range(3):
        for k in range(m + 1):
          if prev_place == curr_place:
            # 같은 장소
            ans[i][curr_place][min(k + l[0][curr_place] // 2, m)] += ans[i - 1][prev_place][k]
            ans[i][curr_place][min(k + l[1][curr_place] // 2, m)] += ans[i - 1][prev_place][k]
          else:
            # 다른 장소
            ans[i][curr_place][min(k + l[0][curr_place], m)] += ans[i - 1][prev_place][k]
            ans[i][curr_place][min(k + l[1][curr_place], m)] += ans[i - 1][prev_place][k]
  
  p(sum(ans[n - 1][i][m] for i in range(3)))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
