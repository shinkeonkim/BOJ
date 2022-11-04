"""
[2108: 통계학](https://www.acmicpc.net/problem/2108)

Tier: Silver 3
Category: 구현
"""


def solution():
  n = int(input())
  l = [int(input()) for _ in range(n)]
  cnt = {}

  for i in l:
    try:
      cnt[i] += 1
    except:
      cnt[i] = 1

  cnt = sorted(cnt.items(), key=lambda t: (-t[1], t[0]))
  ans3 = cnt[0][0]

  if n >= 2 and cnt[0][1] == cnt[1][1]:
    ans3 = cnt[1][0]

  print(int((sum(l) / n * 10 + 5) // 10))
  print(sorted(l)[n // 2])
  print(ans3)
  print(max(l) - min(l))


if __name__ == '__main__':
  solution()
