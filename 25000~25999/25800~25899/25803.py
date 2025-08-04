"""
[25803: Soccer Standing Table](https://www.acmicpc.net/problem/25803)

Tier: Silver 3 
Category: math, bruteforcing, combinatorics
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
  l = mii()
  # 전체 경기수, 승리수, 무승부 수, 패배수, 얻은 점수 순서대로 재배열하여 출력 필요

  for total in range(5):
    for win in range(5):
      for draw in range(5):
        for lose in range(5):
          for score in range(5):
            st = set([total, win, draw, lose, score])
            if len(st) != 5: continue
            if l[total] != l[win] + l[draw] + l[lose]: continue
            if l[score] != l[win] * 3 + l[draw]: continue

            print(f"{l[total]} {l[win]} {l[draw]} {l[lose]} {l[score]}")
            return


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
