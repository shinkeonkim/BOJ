'''
[2909: 캔디 구매](https://www.acmicpc.net/problem/2909)

Tier: Bronze 2
Category: 구현
'''


def solution():
  c, k = map(int, input().split())

  k2 = 10 ** k
  k3 = 10 ** (k - 1) * 5

  c += k3
  c = int(c // k2 * k2)

  return c


if __name__ == '__main__':
  print(solution())
