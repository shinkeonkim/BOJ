"""
[21771: 가희야 거기서 자는 거 아니야](https://www.acmicpc.net/problem/21771)

Tier: Bronze 1
Category: 구현
"""


def solution():
  R, C = map(int, input().split())
  a, b, c, d = map(int, input().split())
  a = a * b
  c = c * d

  m = [input() for i in range(R)]

  p_cnt = sum([m[i].count('P') for i in range(R)])
  g_cnt = sum([m[i].count('G') for i in range(R)])

  if g_cnt != a or (g_cnt == a and p_cnt == c):
    return 0

  return 1


if __name__ == '__main__':
  print(solution())
