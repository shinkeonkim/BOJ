"""
[22183: Приготовление десертов](https://www.acmicpc.net/problem/22183)

Tier: Bronze 1 
Category: bruteforcing, implementation
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


def 반죽_idx(idx):
  return idx

def 속_idx(idx):
  return 100 + idx

def 아이스크림_idx(idx):
  return 200 + idx

def solve():
  n, m, k = map(int, input().split())

  d = defaultdict(lambda: False)

  p = int(input())
  for _ in range(p):
    반죽, 속 = map(int, input().split())
    d[(반죽_idx(반죽), 속_idx(속))] = True
  
  q = int(input())
  for _ in range(q):
    속, 아이스크림 = map(int, input().split())
    d[(속_idx(속), 아이스크림_idx(아이스크림))] = True
  
  r = int(input())
  for _ in range(r):
    반죽, 아이스크림 = map(int, input().split())
    d[(반죽_idx(반죽), 아이스크림_idx(아이스크림))] = True

  ans = 0
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      for k in range(1, k + 1):
        a = 반죽_idx(i)
        b = 속_idx(j)
        c = 아이스크림_idx(k)

        if d[(a, b)] or d[(b, c)] or d[(a, c)]:
          continue
        ans += 1
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
