"""
[25146: KHL](https://www.acmicpc.net/problem/25146)

Tier: Bronze 1 
Category: arithmetic, implementation, math, parsing, string
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


def game(l, home):
  total_score = [0, 0]
  game_cnt = len(l)

  if game_cnt == 3:
    for score in l:
      total_score[home] += score[0]
      total_score[1 - home] += score[1]
  
    if total_score[0] > total_score[1]:
      return 3
    else:
      return 0
  elif game_cnt == 4:
    score = l[-1]
    if home == 1:
      score = score[::-1]
    if score[0] > score[1]:
      return 2
    else:
      return 1
  else:
    score = l[-1]
    if home == 1:
      score = score[::-1]
    if score[0] > score[1]:
      return 1
    else:
      return 0


def solve():
  n = ii()

  ans = 0 # team_0 score
  home = 0
  for _ in range(n):
    l = inp().split("/")
    l = [[*map(int, i.split(":"))] for i in l]
    score = game(l, home)
    home = 1 - home
    ans += score
  
  print(ans)

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
