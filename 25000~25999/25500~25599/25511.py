"""
[25511: 거리가 k이하인 트리 노드에서 사과 수확하기](https://www.acmicpc.net/problem/25511)

Tier: Silver 2
Category: 트리
"""

import sys
# RecursionError: maximum recursion depth exceeded in comparison 에러 방지
sys.setrecursionlimit(10 ** 9)

n = k = 0
adj = []
depth = []
numbers = []


def init():
  global n, k, adj, depth, numbers

  n, k = map(int, input().split())
  adj = [[] for _ in range(n)]
  depth = [-1 for _ in range(n)]

  for _ in range(n - 1):
    a, b = map(int, input().split())

    adj[a].append(b)
    adj[b].append(a)

  numbers = [*map(int, input().split())]


def dfs(node, d):
  depth[node] = d

  for nxt in adj[node]:
    if depth[nxt] == -1:
      dfs(nxt, d + 1)


def solution():
  dfs(0, 0)

  return depth[numbers.index(k)]


if __name__ == '__main__':
  init()
  print(solution())
