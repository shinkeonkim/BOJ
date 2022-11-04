"""
[25785: Easy-to-Pronounce Words](https://www.acmicpc.net/problem/25785)

Tier: Bronze 3
Category: 문자열, 구현
"""


def solution(s):
  prev = -1
  m = 'aeiou'

  for i in s:
    if i in m:
      crt = 0
    else:
      crt = 1

    if crt == prev:
      return 0

    prev = crt

  return 1


if __name__ == '__main__':
  print(solution(input()))
