"""
[20574: General Knight](https://www.acmicpc.net/problem/20574)

Tier: Bronze 1 
Category: math, implementation, data_structures, string, sorting, arithmetic, hash_set
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

def to_axis(s):
  y = ord(s[0]) - ord('a') + 1
  x = int(s[1])

  return (y, x)

def to_str(y, x):
  return chr(y + ord('a') - 1) + str(x)

def solve():
  a, b = mii()
  s = inp()

  dx = [a, a, -a, -a, b, b, -b, -b]
  dy = [b, -b, b, -b, a, -a, a, -a]

  y, x = to_axis(s)
  
  l = []

  for i in range(8):
    ny = y + dy[i]
    nx = x + dx[i]

    if 1 <= ny <= 8 and 1 <= nx <= 8:
      l.append(chr(ny + ord('a') - 1) + str(nx))
  
  l = list(set(l))

  l.sort()

  print(len(l))
  for i in l:
    print(to_str(*to_axis(i)), end= ' ')


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
