"""
[7197: Harmoonia](https://www.acmicpc.net/problem/7197)

Tier: Bronze 1 
Category: arithmetic, bruteforcing, implementation, math
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

def f(crt, nxt, num, k):
  ret = []
  for i in range(k):
    for j in range(i + 1, k):
      if (crt[i] - crt[j]) % 12 != 7:
        continue
      if (nxt[i] - nxt[j]) % 12 != 7:
        continue

      if crt[i] == nxt[i] or crt[j] == nxt[j]:
        continue
      
      ret.append((num, i + 1, j + 1))

  return ret

def solve():
  n, k = mii()
  l = [mii() for _ in range(n)]
  ans = []
  for i in range(0, n - 1):
    ret = f(l[i], l[i + 1], i + 1, k)

    if ret:
      ans.extend(ret)
  
  if ans:
    for i in ans:
      print(*i)
  else:
    print("POLE")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
