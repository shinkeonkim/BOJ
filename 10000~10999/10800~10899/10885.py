"""
[10885: 수열의 장인](https://www.acmicpc.net/problem/10885)

Tier: Platinum 5 
Category: greedy, math
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

MOD = 1000000007

def max_subarray_product(arr):
    n = len(arr)
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    for i in range(1, n):
        if arr[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(arr[i], max_prod * arr[i])
        min_prod = min(arr[i], min_prod * arr[i])
        
        result = max(result, max_prod)
    
    return result % MOD

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + N]))
        index += N
        
        result = max_subarray_product(arr)
        results.append(result)
    
    for res in results:
        print(res)


if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    ret = solve()