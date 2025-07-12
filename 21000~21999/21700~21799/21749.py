"""
[21749: Гистограмма](https://www.acmicpc.net/problem/21749)

Tier: Bronze 1 
Category: implementation, string
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

SYS_INPUT = False
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
  s = ""
  while 1:
    try:
      line = inp()
      s += line + " "
    except:
      break

  s = s.replace(" ", "")
  uniq_s = sorted(list(set(s)))
  cnt = Counter(s)
  max_cnt = max(cnt.values())

  for i in range(max_cnt, 0, -1):
    for c in uniq_s:
      if cnt[c] >= i:
        p(end="#")
      else:
        p(end=" ")
    p()
  
  print("".join(uniq_s))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
