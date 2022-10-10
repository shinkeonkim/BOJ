"""
[15969: 차량 번호판 2](https://www.acmicpc.net/problem/15969)

Tier: Silver 5
Category: 구현
"""


MOD = 1000000009


def solution(s):
  ans = 10 if s[0] == 'd' else 26

  for i in range(1, len(s)):
    prev = s[i - 1]
    crt = s[i]

    if prev == crt:
      ans *= 9 if crt == 'd' else 25
    else:
      ans *= 10 if crt == 'd' else 26

    ans %= MOD

  return ans


if __name__ == '__main__':
  print(solution(input()))
