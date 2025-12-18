"""
[12394: Password Problem (Small)](https://www.acmicpc.net/problem/12394)

Tier: Bronze 1 
Category: math, bruteforcing, probability
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

def get_cnt(A, B, combination, initial_backspace_count):
  if initial_backspace_count == -1:
    return B + 2
  
  
  A2 = A - initial_backspace_count
  ret = initial_backspace_count * 2 + (B - A) + 1


  is_fail = False
  
  for i in range(A2):
    if combination[i]:
      continue
    is_fail = True
  
  if is_fail:
    ret += B + 1
  
  return ret


def solve():
  A, B = mii()
  probabilities = mfi()
  
  expectations = {}

  for i in range(0, 1 << A):
    combinations = []
    
    for j in range(A):
      if i & (1 << j):
        combinations.append(True)
      else:
        combinations.append(False)
    
    probability = 1
    
    for j in range(A):
      if combinations[j]:
        probability *= probabilities[j]
      else:
        probability *= (1 - probabilities[j])

    for backspace_cnt in range(-1, A + 1):
      cnt = get_cnt(A, B, combinations, backspace_cnt)
      # p(combinations, probability, cnt, backspace_cnt)

      expectations[backspace_cnt] = expectations.get(backspace_cnt, 0) + probability * cnt
  return min(expectations.values())


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()

    print(f"Case #{t}: {ret:.6f}")
