"""
[16392: Racing Around the Alphabet](https://www.acmicpc.net/problem/16392)

Tier: Silver 2 
Category: geometry, greedy, implementation, string
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
  K = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
  interval = (2 * pi * 30) / 28
  speed = 15
  
  s = input()
  current = K.index(s[0])
  tm = 1

  for i in range(1, len(s)):
    nxt = K.index(s[i])
    dist = min(abs(current - nxt), 28 - abs(current - nxt)) * interval
    tm += dist / speed + 1
    current = nxt
  
  print(tm)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
