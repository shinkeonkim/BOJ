"""
[25600: Triathlon](https://www.acmicpc.net/problem/25600)

Tier: Bronze 4
Category: 구현
"""


def solution():
  ans = 0
  for i in range(int(input())):
    a, d, g = map(int, input().split())
    s = a * (d + g)
    if a == d + g:
      s = s * 2
    ans = max(ans, s)

  return ans


if __name__ == '__main__':
  print(solution())
