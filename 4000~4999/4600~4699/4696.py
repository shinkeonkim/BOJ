"""
[4696: St. Ives](https://www.acmicpc.net/problem/4696)

Tier: Bronze 4
Category: 구현
"""


def solution():
  while 1:
    a = float(input())
    if a == 0:
      break

    print('%.2f' % (1 + a + a ** 2 + a ** 3 + a ** 4))


if __name__ == '__main__':
  solution()
