"""
[33093: Golden Tickets](https://www.acmicpc.net/problem/33093)

Tier: Bronze 1 
Category: bruteforcing, data_structures, hash_set, implementation, string, set
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
  n, m, k = map(int, input().split())
  
  teams = [input().split() for _ in range(n)]
  
  winner_orgs = set()
  
  for team_name, org_name in teams[:m]:
    winner_orgs.add(org_name)
  
  golden_ticket_teams = []
  
  cnt = 0
  for team_name, org_name in teams[m:]:
    if cnt == k:
      break
    if org_name in winner_orgs:
      continue

    golden_ticket_teams.append(team_name)
    winner_orgs.add(org_name)
    cnt += 1
  
  print(len(golden_ticket_teams))
  print(*golden_ticket_teams, sep="\n")


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
