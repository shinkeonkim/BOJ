"""
[1925: 삼각형](https://www.acmicpc.net/problem/1925)

Tier: Silver 5
Category: 구현
"""


def dis(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def solution():
  l = [[*map(int, input().split())] for _ in range(3)]
  l = sorted([dis(l[i], l[(i + 1) % 3]) for i in range(3)])

  if l[2]**(1 / 2) >= l[0]**(1 / 2) + l[1]**(1 / 2):
    return 'X'

  if l[0] == l[1] == l[2]:
    return 'JungTriangle'

  if l[2] == l[1] or l[1] == l[0]:
    if l[2] == l[1] + l[0]:
      return 'Jikkak2Triangle'

    if l[2] > l[1] + l[0]:
      return 'Dunkak2Triangle'

    return 'Yeahkak2Triangle'

  if l[2] == l[1] + l[0]:
    return 'JikkakTriangle'

  if l[2] > l[1] + l[0]:
    return 'DunkakTriangle'

  return 'YeahkakTriangle'


if __name__ == '__main__':
  print(solution())
