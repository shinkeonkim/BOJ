"""
[10177: Magic Squares](https://www.acmicpc.net/problem/10177)

Tier: Bronze 1
Category: 구현
"""


def solution():
  for _ in range(int(input())):
    n = int(input())
    l = [[*map(int, input().split())] for i in range(n)]
    s = set()

    for i in range(n):
      s.add(sum(l[i]))
      s.add(sum([numbers[i] for numbers in l]))

    s.add(sum([l[i][i] for i in range(n)]))
    s.add(sum([l[n - i - 1][i] for i in range(n)]))

    if len(s) == 1:
      print(f'Magic square of size {n}')
    else:
      print('Not a magic square')


if __name__ == '__main__':
  solution()
