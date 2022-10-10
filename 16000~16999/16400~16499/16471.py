"""
[16471: 작은 수 내기](https://www.acmicpc.net/problem/16471)

Tier: Silver 4
Category: 그리디
"""


def solution():
  cnt = 0
  n = int(input())
  a = sorted([*map(int, input().split())], reverse=True)
  b = sorted([*map(int, input().split())], reverse=True)

  a_i, b_i = 0, 0

  while a_i < n and b_i < n:
    # print(a_i, b_i)
    if a[a_i] < b[b_i]:
      a_i += 1
      b_i += 1
      cnt += 1
    else:
      a_i += 1

  return cnt >= (n + 1) // 2


if __name__ == '__main__':
  print('YES' if solution() else 'NO')
