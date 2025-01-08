"""
[26169: 세 번 이내에 사과를 먹자](https://www.acmicpc.net/problem/26169)

Tier: Silver 3 
Category: backtracking, dfs, graphs, graph_traversal
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
from collections import deque

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
  l = [mii() for _ in range(5)] # 1: 사과, -1: 벽, 0: 빈 공간
  
  r, c = mii() # start point
  
  ans = False
  
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  
  def dfs(current):
    r, c, cnt, move_cnt = current
    
    if cnt >= 2:
      return True
    
    if move_cnt == 3:
      return False
    
    for i in range(4):
      nr, nc = r + dy[i], c + dx[i]
      
      if nr < 0 or nc < 0 or nr >= 5 or nc >= 5 or l[nr][nc] == -1:
        continue
      
      org = l[nr][nc]
      l[nr][nc] = -1
      if dfs([nr, nc, cnt + org, move_cnt + 1]):
        return True
      
      l[nr][nc] = org
    
    return False
  

  org = l[r][c]  
  l[r][c] = -1
  ret = dfs([r, c, org, 0])
  
  print(int(ret))

  

if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()



  # while q:
  #   r, c, cnt, move_cnt = q.popleft()
    
  #   if l[r][c] == 1:
  #     cnt += 1
      
  #   l[r][c] = -1 # 이 조건 때문에 DFS로 해야함.
    
  #   if cnt >= 2:
  #     ans = True
  #     break
    
  #   if move_cnt == 3:
  #     continue
      
  #   for i in range(4):
  #     nr, nc = r + dy[i], c + dx[i]
      
  #     if nr < 0 or nc < 0 or nr >= 5 or nc >= 5 or l[nr][nc] == -1:
  #       continue

  #     q.append([nr, nc, cnt, move_cnt + 1])