"""
[9436: Round Robin](https://www.acmicpc.net/problem/9436)

Tier: Silver 3 
Category: implementation, simulation
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

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)
def near_integer(x): return int(x + 0.5) if x >= 0 else int(x - 0.5)
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]
def transpose(matrix): return list(map(list, zip(*matrix)))

def f(cnt, alive, p, c, start):
  i = start
  turn = 0
  while turn < c:
    turn += 1
    i += 1
    crt = alive[i % p]
    cnt[crt] += 1
  
  next_start_number = alive[(i + 1) % p]
  alive.remove(alive[i % p])
  next_start = (alive.index(next_start_number) - 1 + len(alive)) % len(alive)
  
  return cnt, alive, next_start

def solve(p, c):
  cnt = [0] * p
  alive = [i for i in range(p)]
  
  cnt, alive, next_start = f(cnt, alive, p, c, -1)
  
  while 1:
    # print(cnt, alive, next_start)
    if all(cnt[i] == cnt[alive[0]] for i in alive):
      break
    
    cnt, alive, next_start = f(cnt, alive, len(alive), c, next_start)
  
  return len(alive), cnt[alive[0]]


if __name__ == "__main__":
  while 1:
    s = inp()
    if s == '0':
      break
    
    p, c = map(int, s.split())
    print(*solve(p, c))