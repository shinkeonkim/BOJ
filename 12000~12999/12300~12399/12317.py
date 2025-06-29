"""
[12317: Consonants (Small)](https://www.acmicpc.net/problem/12317)

Tier: Bronze 1 
Category: bruteforcing, implementation
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
  s, n = isplit()
  n = int(n)
  ans = 0

  for start in range(len(s)):
    for end in range(start, len(s)):
      sub_str = s[start:end+1]

      cnt = 0
      for c in sub_str:
        if c not in "aeiou":
          cnt += 1
        else:
          cnt = 0
        
        if cnt >= n:
          ans += 1
          break
      # print(sub_str, cnt)
  
  return ans
        

if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()

    print(f"Case #{t}: {ret}")