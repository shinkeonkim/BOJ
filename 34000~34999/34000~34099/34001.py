"""
[34001: 임스의 일일 퀘스트](https://www.acmicpc.net/problem/34001)

Tier: Bronze 3 
Category: implementation, case_work
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


def solve():
  level = ii()

  table = [
    [
      [200, 210, 220],
      [210, 220, 225],
      [220, 225, 230],
      [225, 230, 235],
      [230, 235, 245],
      [235, 245, 250],
    ],
    [
      [260, 265, 270],
      [265, 270, 275],
      [270, 275, 280],
      [275, 280, 285],
      [280, 285, 290],
      [285, 290, 295],
      [290, 295, 300],
    ]
  ]

  for i in range(2):
    for j in range(len(table[i])):
      need = 0

      if level >= table[i][j][0]:
        need = 500

        if level >= table[i][j][1]:
          need -= 200

      if level >= table[i][j][2]:
        need -= 200
    
      print(need, end=" ")

    print()

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
