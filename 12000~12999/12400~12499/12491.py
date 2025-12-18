"""
[12491: Square Tiles (Small)](https://www.acmicpc.net/problem/12491)

Tier: Silver 4 
Category: greedy, bruteforcing
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
  n, m = mii()
  grid = [input() for _ in range(n)]
  chk = [[''] * m for _ in range(n)]
  
  is_impossible = False
  
  for i in range(n):
    for j in range(m):
      if grid[i][j] == '.':
        chk[i][j] = '.'
      elif chk[i][j] != '':
        continue
      else:
        possible_cnt = 0
        
        for y in range(2):
          for x in range(2):
            if i + y < n and j + x < m and grid[i + y][j + x] == '#' and chk[i + y][j + x] == '':
              possible_cnt += 1
        
        if possible_cnt != 4:
          is_impossible = True
          break
      
        chk[i][j] = '/'
        chk[i][j + 1] = '\\'
        chk[i + 1][j] = '\\'
        chk[i + 1][j + 1] = '/'
  
  if is_impossible:
    print("Impossible")
  else:
    for row in chk:
      print(''.join(row))

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    print(f"Case #{t}:")
    ret = solve()
