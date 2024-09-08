"""
[14713: 앵무새](https://www.acmicpc.net/problem/14713)

Tier: Silver 2 
Category: data_structures, implementation, queue, string
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

SYS_INPUT = True
RECURSION_LIMIT = 10 ** 7
SET_RECURSION = False
BLANK = " "

if SET_RECURSION:
  sys.setrecursionlimit(RECURSION_LIMIT)

inp = lambda : sys.stdin.readline().rstrip() if SYS_INPUT else input()
mii = lambda : [*map(int,inp().split())]
mfi = lambda : [*map(float,inp().split())]
ii = lambda : int(inp())
fi = lambda : float(inp())
isplit = lambda : inp().split()
p = print

def gcd(a, b): return gcd(b, a % b) if b > 0 else a
def lcm(a, b): return a * b // gcd(a, b)


def solve():
  impossible = lambda: print("Impossible")
  
  d = {}
  
  n = ii()
  mx_len = [0] * n
  
  
  for i in range(n):
    sentence = inp().split()
    
    for idx, word in enumerate(sentence):
      d[word] = (i, idx)

    mx_len[i] = len(sentence)
  
  sentence = inp().split()
  
  queue = [[] for _ in range(n)]
  
  for word in sentence:
    if word not in d:
      impossible()
      return
    
    queue[d[word][0]].append(d[word][1])

  for i in range(n):
    if len(queue[i]) != mx_len[i]:
      impossible()
      return
    
    for j in range(0, len(queue[i])):
      if j != queue[i][j]:
        impossible()
        return
    
  print("Possible")



if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()