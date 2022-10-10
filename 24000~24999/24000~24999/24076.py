"""
[24076: IOI 文字列 (IOI String)](https://www.acmicpc.net/problem/24076)

Tier: Bronze 2
Category: 구현
"""


def solution(s):
  return sum([1 if s[i] != 'IO'[i % 2] else 0 for i in range(len(s))])


if __name__ == '__main__':
  input()
  print(solution(input()))
