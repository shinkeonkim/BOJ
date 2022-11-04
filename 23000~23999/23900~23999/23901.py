"""
[23901: Bike Tour](https://www.acmicpc.net/problem/23901)

Tier: Bronze 2
Category: 구현
"""


def solution():
  for tc in range(1, int(input()) + 1):
    cnt = 0
    n = int(input())
    l = [*map(int, input().split())]

    for i in range(1, n - 1):
      if l[i - 1] < l[i] > l[i + 1]:
        cnt += 1

    print(f'Case #{tc}: {cnt}')

  return ''


if __name__ == '__main__':
  print(solution())
