"""
[18126: 너구리 구구](https://www.acmicpc.net/problem/18126)

Tier: Silver 2
Category: 트리, DFS, BFS
"""

import sys
# RecursionError: maximum recursion depth exceeded in comparison 에러 방지
sys.setrecursionlimit(10 ** 9)

n = 0
adj = []
distances = []


def init():
  global n, adj, distances

  n = int(input())
  adj = [[] for _ in range(n + 1)]
  distances = [-1 for _ in range(n + 1)]

  for _ in range(n - 1):
    a, b, d = map(int, input().split())

    adj[a].append([b, d])
    adj[b].append([a, d])


def dfs(node, parent, d):
  distances[node] = d

  for nxt, distance in adj[node]:
    if nxt != parent:
      dfs(nxt, node, distances[node] + distance)


def solution():
  dfs(1, 0, 0)

  return max(distances)


if __name__ == '__main__':
  init()
  print(solution())
