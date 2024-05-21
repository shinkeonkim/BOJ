def solution():
  n, m, *numbers = map(int, open(0).read().split())

  s = sum(numbers)

  crt = 0

  ans = 99999999
  for i in numbers:
    crt += i

    if crt > s // m:
      ans = min(ans, crt)
      crt = 0

  print(ans)


if __name__ == '__main__':
  solution()
