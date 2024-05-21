"""
[9934: 완전 이진 트리](https://www.acmicpc.net/problem/9934)

Tier: Silver 1
Category: 트리, 순회
"""

d = [[] for _ in range(11)]


def dfs(l, depth):
  mid = len(l) // 2
  d[depth].append(l[mid])

  if len(l) == 1:
    return

  dfs(l[:mid], depth + 1)
  dfs(l[mid + 1:], depth + 1)


def solution():
  n = int(input())
  l = [*map(int, input().split())]

  dfs(l, 0)

  for i in range(n):
    print(' '.join([*map(str, d[i])]))


if __name__ == '__main__':
  solution()
