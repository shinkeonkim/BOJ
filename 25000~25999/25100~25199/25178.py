"""
[25178: 두라무리 휴지](https://www.acmicpc.net/problem/25178)

Tier: Silver 5
Category: 구현, 문자열
"""
from re import sub


def solution():
  input()
  a = input()
  b = input()

  if a[0] != b[0] or a[-1] != b[-1]:
    return 'NO'

  if sorted(list(a)) != sorted(list(b)):
    return 'NO'

  a = list(sub('a|e|i|o|u', '', a))
  b = list(sub('a|e|i|o|u', '', b))

  return 'YES' if a == b else 'NO'


if __name__ == '__main__':
  print(solution())
