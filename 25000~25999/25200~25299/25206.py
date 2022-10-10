"""
[25206: 너의 평점은](https://www.acmicpc.net/problem/25206)

Tier: Silver 5
Category: 구현
"""

d = {
  'A+': 4.5,
  'A0': 4.0,
  'B+': 3.5,
  'B0': 3.0,
  'C+': 2.5,
  'C0': 2.0,
  'D+': 1.5,
  'D0': 1.0,
  'F': 0.0,
}


def solution():
  cnt = 0
  total = 0
  while True:
    try:
      _, weight, score = input().split()
    except:
      break

    if score == 'P':
      continue

    weight = float(weight)
    score = d[score]

    cnt += weight
    total += weight * score

  return total / cnt


if __name__ == '__main__':
  print(solution())
