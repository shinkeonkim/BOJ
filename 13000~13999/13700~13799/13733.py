"""
[13733: Square Deal](https://www.acmicpc.net/problem/13733)

Tier: Silver 4 
Category: implementation, bruteforcing, geometry, case_work
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


def solve():
  l = [mii() for _ in range(3)]

  l.sort()

  # 일렬로 나열하는 경우, 한 변이 같아야 한다.

  for i in range(2):
    if l[0][i] in l[1] and l[0][i] in l[2]:
      # 남은 변들의 합
      left_side = l[0][1 - i] + sum(l[1]) + sum(l[2]) - l[0][i] * 2

      if left_side == l[0][i]:
        return "YES"
  
  # 하나의 큰 사각형을 두고, 나머지 2개가 합쳐서 이뤄지는 경우
  max_side = max([*l[0], *l[1], *l[2]])

  for i in range(3):
    if max_side in l[i]:
      left_side = sum(l[i]) - max_side
      need_side_length = max_side - left_side

      k1 = l[(i + 1) % 3]
      k2 = l[(i + 2) % 3]

      if (need_side_length not in k1) or (need_side_length not in k2):
        continue

      k1.remove(need_side_length)
      k2.remove(need_side_length)

      if k1[0] + k2[0] != max_side:
        continue

      return "YES"
  return "NO"


      
if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    p(ret)
