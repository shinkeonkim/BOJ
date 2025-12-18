"""
[7220: Apgavikas](https://www.acmicpc.net/problem/7220)

Tier: Bronze 1 
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
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)
def round_up_half(n): return floor(n + 0.5)
def rotate90(l): return [''.join(x) for x in zip(*l[::-1])]


def solve():
  n, m = mii()
  
  kills = [*map(int, input().split())]
  
  know_imposter = [False] * n
  is_dead = [False] * n
  
  l = [[*map(int, input().split())] for _ in range(n)]
  
  for round in range(n):
    dead_player = kills[round] - 1
    dead_place = l[round][dead_player]
    
    for i in range(n):
      if i == dead_player:
        is_dead[i] = True
        know_imposter[i] = True
        continue
      
      if is_dead[i]:
        continue
      
      if l[round][i] == dead_place:
        know_imposter[i] = True
    
    known_cnt = 0
    unknown_cnt = 1
    
    for i in range(n):
      if is_dead[i]:
        continue
      
      if know_imposter[i]:
        known_cnt += 1
      else:
        unknown_cnt += 1

    if known_cnt > unknown_cnt:
      print(round + 1)
      return
  
  print(n)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
