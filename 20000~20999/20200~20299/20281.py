"""
[20281: Fastminton](https://www.acmicpc.net/problem/20281)

Tier: Bronze 1 
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
  s = input()

  sub_idx = 0
  game_win = [0, 0]
  score = [0, 0]

  is_total_game_finished = False

  for query in s:
    win_idx = 0

    if query == 'Q':
      if is_total_game_finished:
        winner_str = " (winner)"
        print(f"{game_win[0]}{(winner_str if game_win[0] == 2 else '')} - {game_win[1]}{(winner_str if game_win[1] == 2 else '')}")
      else:
        print(f"{game_win[0]} ({score[0]}{('*' if sub_idx == 0 else '')}) - {game_win[1]} ({score[1]}{('*' if sub_idx == 1 else '')})")

    if is_total_game_finished:
      continue
    
    if query == 'S':
      # 서브한 선수가 득점
      score[sub_idx] += 1
      win_idx = sub_idx
    elif query == 'R':
      # 반대 선수가 득점
      score[1 - sub_idx] += 1
      win_idx = 1 - sub_idx
      sub_idx = win_idx
    
    if score[win_idx] == 10 or (score[win_idx] >= 5 and score[win_idx] - score[1 - win_idx] >= 2):
      # 승리 판단 후 해당 게임 종료
      game_win[win_idx] += 1
      score = [0, 0]
      sub_idx = win_idx
    
    if game_win[win_idx] >= 2:
      is_total_game_finished = True


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
