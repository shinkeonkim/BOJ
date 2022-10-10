"""
[18403: KABISA](https://www.acmicpc.net/problem/18403)

Tier: Bronze 2
Category: 구현
"""


def is_leap_year(year):
  return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def solution():
  ans = []

  years = [*map(int, input().split(', '))]

  for year in years:
    if is_leap_year(year):
      ans.append(str(year))

  return ' '.join(ans)


if __name__ == '__main__':
  for tc in range(int(input())):
    print(solution())
