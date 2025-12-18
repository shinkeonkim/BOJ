"""
[7447: Spell checker](https://www.acmicpc.net/problem/7447)

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

def is_similar(word, query):
  if len(word) == len(query):
    diff = 0
    for i in range(len(word)):
      if word[i] != query[i]:
        diff += 1
    return diff == 1

  if len(word) + 1 == len(query):
    for i in range(len(word)):
      if word[i] != query[i]:
        return word[i:] == query[i+1:]
    return True

  if len(word) == len(query) + 1:
    for i in range(len(query)):
      if word[i] != query[i]:
        return word[i+1:] == query[i:]
    return True

  return False

def solve():
  words = []
  queries = []
  
  while 1:
    if (s := input()) == "#":
      break
    words.append(s)

  while 1:
    if (s := input()) == "#":
      break
    queries.append(s)

  for query in queries:
    is_matched = False
    similar_words = []
    for word in words:
      if word == query:
        is_matched = True
        break
      
      if is_similar(word, query):
        similar_words.append(word)
    
    # print(is_matched, similar_words)

    if is_matched:
      p(f"{query} is correct")
    else:
      p(f"{query}: {' '.join(similar_words)}")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()
