"""
[1411: 비슷한 단어](https://www.acmicpc.net/problem/1411)

Tier: Silver 2 
Category: implementation, string, bruteforcing, set
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


def is_similar(a, b):
  need_transition = {}
  
  for i in range(len(a)):
    need_transition[a[i]] = b[i]
      
  if len(need_transition.values()) != len(set(need_transition.values())):
    return False
  
  for i in range(len(a)):
    k = need_transition.get(a[i])
    if k is not None and k != b[i]:
      return False

  return True

def solve():
  n = ii()
  
  words = [inp() for _ in range(n)]
  ans = 0

  for i in range(n):
    for j in range(i + 1, n):
      if is_similar(words[i], words[j]):
        ans += 1

  p(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
