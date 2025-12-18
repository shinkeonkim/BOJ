"""
[3227: MO](https://www.acmicpc.net/problem/3227)

Tier: Silver 5 
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
  p, n = mii()
  l = [ii() for _ in range(n)] # n turn
  
  board = [-1] * p
  
  for i in range(n):
    color = i % 2
    pos = l[i] - 1
    
    left_pos = -1
    
    for j in range(pos):
      if board[j] == color:
        left_pos = j
        
    all_filled = all(board[j] != -1 for j in range(left_pos + 1, pos))
    
    if left_pos != -1 and all_filled:
      for j in range(left_pos + 1, pos):
        board[j] = -1
    
    right_pos = -1
    for j in range(p - 1, pos, -1):
      if board[j] == color:
        right_pos = j
      
    all_filled = all(board[j] != -1 for j in range(pos + 1, right_pos))
    
    if right_pos != -1 and all_filled:
      for j in range(pos + 1, right_pos):
        board[j] = -1
    board[pos] = color
    
  print(board.count(0), board.count(1))


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
