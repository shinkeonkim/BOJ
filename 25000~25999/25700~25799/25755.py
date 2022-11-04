"""
[25755: 거울반사](https://www.acmicpc.net/problem/25755)

Tier: Bronze 2
Category: 구현
"""


def solution():
  w, n = input().split()
  n = int(n)

  l = [[*map(int, input().split())] for i in range(n)]

  if w == 'D' or w == 'U':
    l = l[::-1]
  else:
    for i in range(n):
      l[i] = l[i][::-1]

  D = '?15??2??8?'

  for m in l:
    for i in m:
      print(D[i], end=' ')
    print()


if __name__ == '__main__':
  solution()
