"""
[200001: 고무오리 디버깅](https://www.acmicpc.net/problem/200001)

Tier: Bronze 1
Category: 스택
"""


def solution():
  input()
  cnt = 0

  while 1:
    s = input()

    if s == '고무오리 디버깅 끝':
      break

    if s == '문제':
      cnt += 1

    if s == '고무오리':
      if cnt > 0:
        cnt -= 1
      else:
        cnt += 2

  if cnt == 0:
    return '고무오리야 사랑해'

  return '힝구'


if __name__ == '__main__':
  print(solution())
