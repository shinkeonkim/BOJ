"""
[26743: Oczko](https://www.acmicpc.net/problem/26743)

Tier: Silver 5 
Category: implementation, string
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

def deck_score(deck):
  ret = 0
  ace = 0
  for i in deck:
    if i == 'A':
      ace += 1
    elif i in 'TJQK':
      ret += 10
    else:
      ret += "--23456789".index(i)
  
  while ace > 0:
    if ret + (ace - 1) + 11 <= 21:
      ret += 11
    else:
      ret += 1
    ace -= 1
  
  return ret


def solve():
  n = ii()
  player_decks = [inp() for _ in range(n)]
  scores = [deck_score(deck) for deck in player_decks]
  
  winner_score = -1
  
  for score in scores:
    if score > 21:
      continue
    winner_score = max(winner_score, score)
  
  winners = []
  for i in range(n):
    if scores[i] == winner_score:
      winners.append(i + 1)
  
  print(len(winners))
  print(*winners)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
