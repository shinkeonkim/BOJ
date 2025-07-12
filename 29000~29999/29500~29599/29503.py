"""
[29503: Шахматы](https://www.acmicpc.net/problem/29503)

Tier: Bronze 2 
Category: implementation, parsing, simulation, string
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
  return ord(s[0]) - ord('a'), 8 - int(s[1])

def solve():
  board = [list(inp()) for _ in range(8)]

  n = ii()

  for _ in range(n):
    command = inp()
    a, b = command[:2], command[2:]
    a_x, a_y = to_axis(a)
    b_x, b_y = to_axis(b)

    moving = board[a_y][a_x]

    board[a_y][a_x] = '.'
    board[b_y][b_x] = moving

    print(moving, end='')


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
