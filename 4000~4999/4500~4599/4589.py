"""
[4589: Gnome Sequencing](https://www.acmicpc.net/problem/4589)

Tier: Bronze 4
Category: 구현
"""


def solution():
  tc = int(input())
  print('Gnomes:')

  for _ in range(tc):
    l = [*map(int, input().split())]

    if sorted(l) == l or sorted(l, reverse=True) == l:
      print('Ordered')
    else:
      print('Unordered')


if __name__ == '__main__':
  solution()
