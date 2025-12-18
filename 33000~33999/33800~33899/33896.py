"""
[33896: 아깝게 놓친 COSS 장학금](https://www.acmicpc.net/problem/33896)

Tier: Silver 5 
Category: math, implementation, sorting
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
from dataclasses import dataclass


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

@dataclass
class Student:
  name: str
  score: int
  risk: int
  cost: int
  
  def scholarship_score(self):
    return int(self.score ** 3 / (self.cost * (self.risk + 1)))
  
  def __init__(self, s):
    l = s.split()
    self.name = l[0]
    self.score = int(l[1])
    self.risk = int(l[2])
    self.cost = int(l[3])

  def __lt__(self, other):
    if self.scholarship_score() != other.scholarship_score():
      return self.scholarship_score() > other.scholarship_score()

    if self.cost != other.cost:
      return self.cost < other.cost

    return self.name < other.name


def solve():
  n = ii()
  print(sorted([Student(input()) for _ in range(n)])[1].name)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
