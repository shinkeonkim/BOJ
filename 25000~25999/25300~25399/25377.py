INF = 999999999999


def solution(numbers):
  ans = INF

  for a, b in numbers:
    if a <= b:
      ans = min(b, ans)

  return -1 if ans == INF else ans


if __name__ == '__main__':
  print(solution([[*map(int, input().split())] for _ in range(int(input()))]))
