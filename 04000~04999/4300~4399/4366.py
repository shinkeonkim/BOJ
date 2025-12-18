"""
[4366: Average Speed](https://www.acmicpc.net/problem/4366)

Tier: Bronze 1 
Category: math, implementation, string, arithmetic, parsing
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

SYS_INPUT = False
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

def to_num(time_str):
  h, m, s = map(int, time_str.split(":"))
  return h * 3600 + m * 60 + s


def solve():
  distance = 0
  last_time = 0
  current_speed = 0

  while 1:
    try:
      s = inp()
    except EOFError:
      break
    
    if " " in s:
      # 속도 변경 쿼리
      time, speed = s.split()
      time = to_num(time)
      speed = int(speed) / 3600

      if last_time == 0:
        # 첫 쿼리인 경우
        last_time = time
        current_speed = speed
        continue

      distance += (time - last_time) * current_speed
      current_speed = speed
      last_time = time
    else:
      # 현재까지 이동 거리 조회
      p(s, f"{distance + (to_num(s) - last_time) * current_speed:.2f} km")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
