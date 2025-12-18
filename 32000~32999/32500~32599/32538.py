"""
[32538: Battle of Nieuwpoort](https://www.acmicpc.net/problem/32538)

Tier: Bronze 1 
Category: implementation, math, string
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

def to_c(n):
  if n < 10:
    return str(n)
  else:
    return chr(ord('a') + n - 10)

def convert_base(n, b):
  ret = ""
  while n > 0:
    ret = to_c(n % b) + ret
    n //= b
  return ret if ret else "0"

def solve():
  year = int(inp().split()[0])

  for i in range(2, 17):
    k = convert_base(year, i)

    if k[-2:] == "00":
      print(i, k)
      return
  print("impossible")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
