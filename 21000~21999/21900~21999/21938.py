"""
[21938: 영상처리](https://www.acmicpc.net/problem/21938)

Tier: Silver 2 
Category: bfs, dfs, graphs, graph_traversal
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
  n, m = mii()
  
  rgb = [mii() for _ in range(n)]
  
  T = ii() # 경계값
  
  l = [[0] * m for _ in range(n)]
  
  for i in range(n):
    for j in range(m):
      if sum(rgb[i][3 * j:3 * j + 3]) >= T  * 3:
        l[i][j] = 1
      else:
        l[i][j] = 0
  
  ans = 0
  
  chk = [[0] * m for _ in range(n)]
  
  for i in range(n):
    for j in range(m):
      if chk[i][j] == 0 and l[i][j]:
        ans += 1
        
        q = []
        
        q.append((i, j))
        
        while q:
          y, x = q.pop()
          
          chk[y][x] = 1
          
          for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y + dy, x + dx
            
            if ny < 0 or ny >= n or nx < 0 or nx >= m or chk[ny][nx] or l[ny][nx] == 0:
              continue
            q.append((ny, nx))
  
  print(ans)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()