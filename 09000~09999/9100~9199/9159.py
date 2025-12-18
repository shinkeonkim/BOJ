"""
[9159: What is the air speed velocity...](https://www.acmicpc.net/problem/9159)

Tier: Bronze 1 
Category: arithmetic, implementation, math
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


def solve():
  A_d, E_d = mii()

  times = defaultdict(int)
  velocities = defaultdict(int)
  
  for _ in range(20):
    a, b = input().split()
    a = a.lower()
    b = float(b)
    
    times[a] += b
    distance = A_d if a == 'a' else E_d
    velocities[a] += distance / b
  
  print("Method 1")
  print(f"African: {10 * A_d / times['a']:.2f} furlongs per hour")
  print(f"European: {10 * E_d / times['e']:.2f} furlongs per hour")
  print("Method 2")
  print(f"African: {velocities['a'] / 10:.2f} furlongs per hour")
  print(f"European: {velocities['e'] / 10:.2f} furlongs per hour")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
