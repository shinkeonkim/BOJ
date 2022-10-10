"""
[25630: 팰린드롬 소떡소떡](https://www.acmicpc.net/problem/25630)

Tier: Bronze 3
Category: 구현
"""


def solution(s):
  cnt = 0

  for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
      cnt += 1

  return cnt


if __name__ == '__main__':
  input()
  print(solution(input()))
