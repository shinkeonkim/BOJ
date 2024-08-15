"""
[12891: DNA 비밀번호](https://www.acmicpc.net/problem/12891)

Tier: Silver 2 
Category: sliding_window, string
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


def solve():
  s, p = mii()
  dna = inp()
  cnt = mii() # A, C, G, T
  
  crt = {'A':0, 'C':0, 'G':0, 'T':0}
  
  ans = 0
  
  dna_idx = {'A':0, 'C':1, 'G':2, 'T':3}
  
  for i in range(s):
    crt[dna[i]] += 1
    
    if i >= p:
      crt[dna[i-p]] -= 1
    
    if i >= p-1 and all([crt[key] >= cnt[dna_idx[key]] for key in crt.keys()]):
      ans += 1
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()