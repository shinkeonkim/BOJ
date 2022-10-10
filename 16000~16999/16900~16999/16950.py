"""
[16960: 스위치와 램프](https://www.acmicpc.net/problem/16960)

Tier: Silver 4
Category: 구현
"""


def solution():
  n, m = map(int, input().split())
  cnt = [0] * (m + 1)
  ar = []

  for _ in range(n):
    l = [*map(int, input().split())]
    l = l[1:]
    ar.append(l)

    for num in l:
      cnt[num] += 1

  for numbers in ar:
    for number in numbers:
      if cnt[number] == 1:
        break
    else:
      return 1

  return 0


if __name__ == '__main__':
  print(solution())
