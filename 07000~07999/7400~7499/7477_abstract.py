"""
[7477: Highways](https://www.acmicpc.net/problem/7477)

Tier: Bronze 1 
Category: greedy
"""
from heapq import heappush, heappop

def solve():
  n = int(input())
  k = [*map(int, input().split())]
  
  if n <= 3:
    print(0)
    return

  q = []
  sm = 0
  prev = 0
  for i in range(n - 1):
    heappush(q, (k[i] - prev, i))
    sm += (k[i] - prev)
    prev = k[i]
  
  selected = -1
  while 1:
    front = heappop(q)
    if front[1] == 0 or front[1] == n - 2: continue
    
    sm += front[0]
    selected = front[1]
    break
  
  print(sm)
  print(selected + 2, 1, n, selected + 1)

solve()