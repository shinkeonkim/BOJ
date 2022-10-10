"""
[11725: 트리의 부모 찾기](https://www.acmicpc.net/problem/11725)

Tier: Silver 2
Category: 트리
"""

import sys
# RecursionError: maximum recursion depth exceeded in comparison 에러 방지
sys.setrecursionlimit(10 ** 9)

n = k = 0
adj = []
parent = []


def init():
  global n, adj, parent

  n = int(input())
  adj = [[] for _ in range(n + 1)]
  parent = [-1 for _ in range(n + 1)]

  for _ in range(n - 1):
    a, b = map(int, input().split())

    adj[a].append(b)
    adj[b].append(a)


def dfs(node, prev):
  parent[node] = prev

  for nxt in adj[node]:
    if parent[nxt] == -1:
      dfs(nxt, node)


def solution():
  dfs(1, 0)

  for i in range(2, n + 1):
    print(parent[i])


if __name__ == '__main__':
  init()
  solution()
