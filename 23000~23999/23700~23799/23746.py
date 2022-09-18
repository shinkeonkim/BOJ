d = {}

for i in range(int(input())):
  v, k = input().split()
  d[k] = v

s = input()
start, end = map(int, input().split())

s2 = ''

for i in s:
  s2 += d[i]

print(s2[(start - 1):end])
