"""
[7830: Romantic Date](https://www.acmicpc.net/problem/7830)

Tier: Silver 3 
Category: implementation, greedy
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


d = {
  'T': 9,
  'A': 13,
  'K': 12,
  'Q': 11,
  'J': 10,
}

def card_to_num(s):
  if s[0] not in d:
    num = int(s[0]) - 1
  else:
    num = d[s[0]]
  shape = 'DCHS'.index(s[1])

  return (num - 1) * 4 + shape


def solve():
  l = [*map(card_to_num, input().split())]

  left = list(set([i for i in range(52)]) - set(l))
  left.sort()
  l.sort()

  i = j = 0
  ans = 0

  while i < 26 and j < 26:
    if l[i] > left[j]:
      ans += 1
      i += 1
      j += 1
    else:
      i += 1

  print(ans)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
