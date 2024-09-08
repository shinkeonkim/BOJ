"""
[19583: 싸이버개강총회](https://www.acmicpc.net/problem/19583)

Tier: Silver 2 
Category: data_structures, hash_set, implementation, string
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

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

def str_to_tm(s):
  h, m = map(int, s.split(":"))
  return h*60 + m


def solve():
  d = {} #
  
  s, e, q = map(str_to_tm, isplit())
  
  # s보다 작은 경우 => 1 e와 q 사이에 있는 경우 => 2 -> OR 연산으로 d에 추가
  
  while True:
    try:
      t, name = isplit()
      t = str_to_tm(t)
      
      if t <= s:
        d[name] = d.get(name, 0) | 1
      elif t >= e and t <= q:
        d[name] = d.get(name, 0) | 2
    except:
      break
  
  ret = 0
  for v in d.values():
    if v == 3:
      ret += 1
  
  p(ret)
  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()