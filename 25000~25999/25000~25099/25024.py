"""
[25024: 시간과 날짜](https://www.acmicpc.net/problem/25024)

Tier: Bronze 3
Category: 구현
"""


def is_valid_time(h, m):
  return 0 <= h <= 23 and 0 <= m <= 59


def is_valid_day(m, d):
  if m < 1 or m > 12 or d < 1:
    return False

  if m == 2:
    return d <= 29

  if m in [1, 3, 5, 7, 8, 10, 12]:
    return d <= 31

  return d <= 30


def bool_str(b: bool) -> str:
  return 'Yes' if b else 'No'


def solution():
  for _ in range(int(input())):
    a, b = map(int, input().split())
    print(f'{bool_str(is_valid_time(a, b))} {bool_str(is_valid_day(a, b))}')


if __name__ == '__main__':
  solution()
