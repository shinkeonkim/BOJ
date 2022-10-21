"""
[25642: 젓가락 게임](https://www.acmicpc.net/problem/25642)

Tier: Bronze 3
Category: 구현
"""


def solution():
  a, b = map(int, input().split())

  t = 0
  while a < 5 and b < 5:
    if t % 2 == 0:
      b += a
    else:
      a += b

    t += 1

  if t % 2 == 0:
    return 'yj'

  return 'yt'


if __name__ == '__main__':
  print(solution())
