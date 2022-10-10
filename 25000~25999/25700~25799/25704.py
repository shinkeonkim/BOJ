"""
[25704: 출석 이벤트](https://www.acmicpc.net/problem/25704)

Tier: Bronze 4
Category: 구현
"""


def solution():
  n = int(input())
  p = int(input())
  l = [p]

  if n >= 5:
    l.append(p - 500)

  if n >= 10:
    l.append(p * 9 // 10)

  if n >= 15:
    l.append(p - 2000)

  if n >= 20:
    l.append(p * 3 // 4)

  return max(0, min(l))


if __name__ == '__main__':
  print(solution())
