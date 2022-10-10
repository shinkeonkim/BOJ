"""
[5636: 소수 부분 문자열](https://www.acmicpc.net/problem/5636)

Tier: Silver 1
Category: 문자열, 소수
"""

MAX_N = 1000001


def solution():
  D = [True for _ in range(MAX_N)]
  # D[i] : i가 소수인지 여부를 저장함.

  D[0] = D[1] = False

  # 에라토스테네스의 채 구현
  for i in range(2, MAX_N):
    if D[i]:
      for j in range(i + i, MAX_N, i):
        D[j] = False

  # 문제 내용 구현
  while True:
    s = input()
    ans = 0

    if s == '0':
      # 종료 조건
      break

    for start in range(len(s)):
      for k in range(start, min(start + 5, len(s))):
        crt = int(s[start:k + 1])
        if crt <= MAX_N - 1 and D[crt]:
          # 현재 숫자가 최대 범위를 벗어나지 않으면서, 소수인가?
          ans = max(ans, crt)

    print(ans)


if __name__ == '__main__':
  solution()
