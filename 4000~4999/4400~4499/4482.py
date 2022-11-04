"""
[4482: Tetrahedral Stacks of Cannonballs](https://www.acmicpc.net/problem/4482)

Tier: Bronze 2
Category: 구현
"""


def solution():
  D = [0, 1, 4]
  ar = [0, 1, 3]

  for i in range(3, 1001):
    ar.append(ar[i - 1] + i)
    D.append(D[i - 1] + ar[i])

  for tc in range(1, int(input()) + 1):
    a = int(input())
    print(f'{tc}: {a} {D[a]}')


if __name__ == '__main__':
  solution()
