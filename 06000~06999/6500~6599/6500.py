"""
[6500: 랜덤 숫자 만들기](https://www.acmicpc.net/problem/6500)

Tier: Bronze 2
Category: 구현
"""


def solution():
  while 1:
    n = int(input())
    if n == 0:
      break

    d = {}

    while d.get(n, False) == False:
      d[n] = True

      n = str(n * n)

      n = (8 - len(n)) * '0' + n

      n = int(n[2:6])

    print(len(d))


if __name__ == '__main__':
  solution()
