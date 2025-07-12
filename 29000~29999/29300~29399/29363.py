"""
[29363: Пишущая машинка](https://www.acmicpc.net/problem/29363)

Tier: Bronze 2 
Category: math, greedy, string
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
  n = ii()

  l = [inp() for _ in range(n)]

  ans = len(l[0])

  for i in range(1, n):
    # 방법 1
    # 처음부터 그냥 다 쓰기

    ans += 1

    current = len(l[i])
    # 방법 2
    # 이전 문장을 복사한 후, 뒤에서부터 다른 문자를 다 지우고 다시 작성

    differnt_idx = -1

    for j in range(0, min(len(l[i]), len(l[i-1]))):
      if l[i][j] != l[i-1][j]:
        differnt_idx = j
        break

    if differnt_idx == -1:
      if len(l[i]) > len(l[i-1]):
        delete_count = 0
        add_count = len(l[i]) - len(l[i-1])
      else:
        delete_count = len(l[i-1]) - len(l[i])
        add_count = 0
    else:
      delete_count = len(l[i - 1]) - differnt_idx
      add_count = len(l[i]) - differnt_idx

    current = min(current, delete_count + add_count + 1)
    ans += current
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
