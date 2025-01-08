"""
[30924: A+B - 10 (제2편)](https://www.acmicpc.net/problem/30924)

Tier: Silver 5 
Category: arithmetic, math, randomization
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
from random import randint

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
  ans_a = -1
  ans_b = -1
  
  a = {}
  b = {}  

  while len(a) < 9999:
    i = randint(1, 10000)
    
    if a.get(i) is None:
      a[i] = 1
    else:
      continue
    
    print(f"? A {i}", flush=True)
    k = ii()
    
    if k == 1:
      ans_a = i
      break

  while len(b) < 9999:
    i = randint(1, 10000)
    
    if b.get(i) is None:
      b[i] = 1
    else:
      continue
    
    print(f"? B {i}", flush=True)
    k = ii()
    
    if k == 1:
      ans_b = i
      break
    
  print(f"! {ans_a + ans_b}")

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()