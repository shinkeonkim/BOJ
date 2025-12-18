"""
[21032: Odd GCD Matching](https://www.acmicpc.net/problem/21032)

Tier: Silver 2 
Category: greedy, math, number_theory
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
  # GCD가 홀수인 쌍의 개수
  # 짝수 <-> 짝수는 절대 할 수 없다.
  # 홀 <-> 짝 가능, 홀 <-> 홀 가능

  n = ii()
  l = mii()

  odd_cnt = 0
  even_cnt = 0

  for i in l:
    if i % 2 == 0:
      even_cnt += 1
    else:
      odd_cnt += 1
  
  # 일단 짝수를 쳐낸다.
  ans = 0

  k = min(odd_cnt, even_cnt)
  ans += k
  odd_cnt -= k
  even_cnt -= k

  # 홀끼리 쌍을 만든다.
  ans += odd_cnt // 2

  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
