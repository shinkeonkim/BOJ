"""
[4201: Snakes and Ladders](https://www.acmicpc.net/problem/4201)

Tier: Bronze 2 
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
  n, b, c = map(int, inp().split())
  l = [[*map(int, inp().split())] for _ in range(b)]
  d = defaultdict(lambda: -1)
  
  for a, b in l:
    d[a] = b

  dices = [int(inp()) for _ in range(c)]
  
  positions = [1] * n
  
  turn = 0
  
  for dice in dices:
    positions[turn] += dice
    
    while d[positions[turn]] != -1:
      positions[turn] = d[positions[turn]]

    if positions[turn] >= 100:
      positions[turn] = 100
      break
    
    turn = (turn + 1) % n
  
  for i in range(n):
    print(f"Position of player {i + 1} is {positions[i]}.")
    

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
