"""
[4779: 칸토어 집합](https://www.acmicpc.net/problem/4779)

Tier: Silver 3 
Category: divide_and_conquer, recursion
"""

DP = ["" for _ in range(13)]

def f(n : int) -> str:
  """N 번째 칸토어 집합의 근사를 출력하는 함수"""

  if DP[n] != "":
    # N 번째 칸토어 집합이 이미 계산되어 있다면, 해당 값을 반환
    return DP[n]
  
  # N 번째 칸토어 집합을 계산하고 저장
  DP[n] = f(n - 1) + " " * (3 ** (n-1)) + f(n - 1)
  
  return DP[n] # N 번째 칸토어 집합 반환


DP[0] = "-" # 0 번째 칸토어 집합은 "-" 로 초기화
  
while 1:
  # 파일의 끝에서 입력을 멈추기 위한 무한 루프 및 예외처리
  try:
    n = int(input()) # N 입력
  except:
    break
  
  print(f(n)) # N 번째 칸토어 집합 출력
  print(len(f(n)))

