def solution(s, m):
  if s < 1024:
    return 'No thanks'

  d = s - 1023
  k = 512

  while k > 0:
    if m >= k:
      m -= k
      if d >= k:
        d -= k

    k //= 2

  if d > 0:
    return 'Impossible'

  return 'Thanks'


s, m = map(int, input().split())
print(solution(s, m))
