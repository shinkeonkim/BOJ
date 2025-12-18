"""
[4396: 지뢰 찾기](https://www.acmicpc.net/problem/4396)

Tier: Silver 4 
Category: implementation
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
  n = ii()
  
  result = [input() for _ in range(n)]
  board = [input() for _ in range(n)]
  dy = [0, 0, 1, -1, 1, 1, -1, -1]
  dx = [1, -1, 0, 0, 1, -1, 1, -1]
  
  gameover = False
  for i in range(n):
    for j in range(n):
      if board[i][j] == 'x' and result[i][j] == '*':
        gameover = True
  
  for i in range(n):
    ret = ""
    for j in range(n):
      if gameover and result[i][j] == '*':
        ret += '*'
        continue
      if board[i][j] == '.':
        ret += '.'
        continue
      cnt = 0
      for d in range(8):
        ny = i + dy[d]
        nx = j + dx[d]
        
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
          continue
        
        if result[ny][nx] == '*':
          cnt += 1
      
      ret += str(cnt)

    print(ret)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
