"""
[4855: Tire Dimensions](https://www.acmicpc.net/problem/4855)

Tier: Bronze 2 
Category: arithmetic, implementation, math, parsing, string
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
  while 1:
    try:
      s = input()
    except EOFError:
      break
  
    l = s.split()

    section_width = int(l[1])
    ratio = int(l[3])
    nominal_rim_diameter = int(l[-1]) * 25.4

    section_height = section_width * ratio / 100
    overall_diameter = nominal_rim_diameter + 2 * section_height

    radius = overall_diameter / 2

    ans = round(2 * pi * radius / 10)
    print(f"{s}: {ans}")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
