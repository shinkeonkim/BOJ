"""
[21895: Rock-Paper-Scissors for three](https://www.acmicpc.net/problem/21895)

Tier: Bronze 2
Category: 구현
"""

d = {
  'RR': 'P',
  'SS': 'R',
  'PP': 'S',
  'PR': 'P',
  'RS': 'R',
  'PS': 'S',
}


def solution():
  ans = ''
  n = int(input())
  a = input()
  b = input()

  for i in range(n):
    ans += d[''.join(sorted([a[i], b[i]]))]

  return ans


if __name__ == '__main__':
  print(solution())
