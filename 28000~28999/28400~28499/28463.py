"""
[28463: Toe Jumps](https://www.acmicpc.net/problem/28463)

Tier: Silver 5 
Category: case_work, implementation
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


def rotate90(l):
  return [''.join(x) for x in zip(*l[::-1])]

def rotate(l, count):
  for _ in range(count):
    l = rotate90(l)
  return l

def rotate_count(c):
  s = 'SENW'
  return s.index(c)

def solve():
  direction = input()
  l = [input() for _ in range(2)]

  l = rotate(l, rotate_count(direction))

  if l[0] =='.O' and l[1] == 'P.':
    return 'T'

  if l[0] == 'I.' and l[1] == '.P':
    return 'F'
  
  if l[0] == 'O.' and l[1] == '.P':
    return 'Lz'

  return '?'


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
    print(ret)
