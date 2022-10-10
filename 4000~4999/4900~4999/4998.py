"""
[4998: 저금](https://www.acmicpc.net/problem/4998)

Tier: Bronze 2
Category: 구현
"""


def solution(money, per, target):
  ans = 0
  while money < target:
    ans += 1
    money = money + (per / 100) * money

  return ans


if __name__ == '__main__':
  while 1:
    try:
      print(solution(*map(float, input().split())))
    except:
      break
