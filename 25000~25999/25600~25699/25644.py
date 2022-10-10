"""
[25644: 최대 상승](https://www.acmicpc.net/problem/25644)

Tier: Silver 5
Category: 그리디
"""


def solution():
  n = int(input())
  prices = [*map(int, input().split())]

  mn = prices[0]  # 최소값
  ans = 0

  for i in range(1, n):
    mn = min(mn, prices[i])
    # [0, i] 까지의 최소값을 계속해서 갱신합니다.
    ans = max(ans, prices[i] - mn)
    # 최대 이득을 갱신합니다.

  return ans


if __name__ == '__main__':
  print(solution())
