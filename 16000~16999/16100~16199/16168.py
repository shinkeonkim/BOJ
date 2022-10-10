"""
[16168: 퍼레이드](https://www.acmicpc.net/problem/16168)

Tier: Gold 4
Category: 구현
"""
import sys
sys.setrecursionlimit(10**6)


MAX_V = 3300
used_edge = 0

path = []
adj = [[0] * MAX_V for _ in range(MAX_V)]


def eulerPathSearch(node: int, n: int):
  global used_edge

  for i in range(n + 1):
    while adj[node][i] > 0:
      adj[node][i] -= 1
      adj[i][node] -= 1
      used_edge += 1
      eulerPathSearch(i, n)


def solution():
  n, m = map(int, input().split())
  cnt = [0] * (n + 1)

  for i in range(m):
    a, b = map(int, input().split())
    cnt[a] += 1
    cnt[b] += 1
    adj[a][b] += 1
    adj[b][a] += 1

  cnt = sum([i % 2 for i in cnt])

  if cnt != 0 and cnt != 2:
    return 'NO'

  eulerPathSearch(1, n)

  if used_edge == m:
    return 'YES'

  return 'NO'


if __name__ == '__main__':
  print(solution())
