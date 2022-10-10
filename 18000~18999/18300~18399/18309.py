"""
[18309: Extreme Temperatures](https://www.acmicpc.net/problem/18309)

Tier: Bronze 2
Category: 구현
"""


def solution():
  temperatures = []
  while 1:
    try:
      _, *temps = input().split()
    except:
      break
    temperatures.extend([*map(int, temps)])

  return f'{min(temperatures)} {max(temperatures)}'


if __name__ == '__main__':
  print(solution())
