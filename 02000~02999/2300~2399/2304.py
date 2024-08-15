"""
[2304: 창고 다각형](https://www.acmicpc.net/problem/2304)

Tier: Silver 2 
Category: bruteforcing, data_structures, stack
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
  n = ii()
  l = [mii() for _ in range(n)] # 각 기둥의 위치와 높이
  
  l.sort() # 위치 순으로 정렬
  
  # 왼쪽에서 오른쪽으로 가면서 가장 높은 기둥을 찾는다.
  mx_idx = 0
  for i in range(n):
    if l[i][1] > l[mx_idx][1]:
      mx_idx = i
  
  # 왼쪽에서 가장 높은 기둥까지의 면적을 구한다.
  
  area = 0
  h = l[0][1]
  for crt in range(1, mx_idx+1):
    if crt > 0:
      area += h * (l[crt][0] - l[crt-1][0])

    if l[crt][1] > h:
      h = l[crt][1]
    
  h = l[n-1][1]
  for crt in range(n-2, mx_idx-1, -1):
    if crt + 1 < n:
      area += h * (l[crt+1][0] - l[crt][0])

    if l[crt][1] > h:
      h = l[crt][1]
    
  
  p(area + l[mx_idx][1])
  


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()