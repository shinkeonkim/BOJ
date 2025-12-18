"""
[26578: Word](https://www.acmicpc.net/problem/26578)

Tier: Silver 2 
Category: bruteforcing
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
  n, m = mii()
  l = [inp() for _ in range(n)]
  s = []

  for i in range(n):
    s.append(l[i])
  
  for j in range(m):
    temp = ""
    for i in range(n):
      temp += s[i][j]
    s.append(temp)
  
  for i in range(n - 3):
    for j in range(m - 3):
      temp = ""
      for d in range(4):
        temp += s[i + d][j + d]
      s.append(temp)
  
  for i in range(n - 3):
    for j in range(3, m):
      temp = ""
      for d in range(4):
        temp += s[i + d][j - d]
      s.append(temp)
  
  s = " ".join(s)

  print(s.count("word") + s.count("drow"))


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
