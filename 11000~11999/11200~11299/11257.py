"""
[11257: IT Passport Examination](https://www.acmicpc.net/problem/11257)

Tier: Bronze 4
Category: 구현
"""


def solution():
  for i in range(int(input())):
    no, a, b, c = map(int, input().split())

    chk = True
    s = a + b + c

    if s < 55 or a * 100 < 30 * 35 or b * 100 < 30 * 25 or c * 100 < 30 * 40:
      chk = False

    print(no, s, 'PASS' if chk else 'FAIL')


if __name__ == '__main__':
  solution()
