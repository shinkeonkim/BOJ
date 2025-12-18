"""
[3961: 터치스크린 키보드](https://www.acmicpc.net/problem/3961)

Tier: Silver 2 
Category: implementation, string, sorting
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

keys = [
  "qwertyuiop",
  "asdfghjkl",
  "zxcvbnm"
]

def position(ch):
  for i in range(3):
    for j in range(len(keys[i])):
      if keys[i][j] == ch:
        return (i, j)

def diff(a, b):
  ret = 0
  for i in range(len(a)):
    pos_a = position(a[i])
    pos_b = position(b[i])
    ret += abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])
  return ret

def solve(): 
  word, n = isplit()
  n = int(n)
  
  ans = []
  for _ in range(n):
    target = inp()
    ans.append((diff(word, target), target))
  
  ans.sort()

  for d, target in ans:
    print(target, d)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()
