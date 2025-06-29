"""
[1680: 쓰레기 수거](https://www.acmicpc.net/problem/1680)

Tier: Silver 3 
Category: implementation, simulation
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

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


def solve():
  W, N = mii() # W: 용량, N : 지점의 개수

  trashes = [mii() for _ in range(N)]

  distance = 0
  current_trash = 0
  current_position = 0

  for idx in range(N):
    position, trash = trashes[idx]
  
    distance += position - current_position
    current_position = position
    current_trash += trash
  
    if current_trash > W:
      # 그 지점의 쓰레기를 실었을 때 쓰레기차의 용량을 넘게 될 때, 다시 원점으로 돌아가서 놓고 왔다고 가정
      distance += 2 * position
      current_trash = trash

    if current_trash == W:
      # 현재 쓰레기 양이 용량과 같으면, 다시 원점으로 돌아가서 놓고 왔다고 가정
      distance += position
      current_position = 0
      current_trash = 0    
  
  distance += current_position
  print(distance)


if __name__ == "__main__":
  tc = ii()
  for t in range(1, tc+1):
    ret = solve()