'''
[12005: Diamond Collector (Bronze)](https://www.acmicpc.net/problem/12005)

Tier: Silver 5
Category: 정렬
'''


def solution():
  ans = 0

  n, k = map(int, input().split())
  numbers = sorted([int(input()) for _ in range(n)])

  l = r = 0

  while l <= r and r < n:
    diff = numbers[r] - numbers[l]

    if diff <= k:
      ans = max(ans, r - l + 1)
      r += 1
    else:
      l += 1

  return ans


if __name__ == '__main__':
  print(solution())
