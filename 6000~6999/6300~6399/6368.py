"""
[6368: P,MTHBGWB](https://www.acmicpc.net/problem/6368)

Tier: Bronze 1
Category: 구현
"""


import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

morse_code_dict = {
  'A': '01', 'B': '1000', 'C': '1010', 'D': '100', 'E': '0',
  'F': '0010', 'G': '110', 'H': '0000', 'I': '00', 'J': '0111',
  'K': '101', 'L': '0100', 'M': '11', 'N': '10', 'O': '111',
  'P': '0110', 'Q': '1101', 'R': '010', 'S': '000', 'T': '1',
  'U': '001', 'V': '0001', 'W': '011', 'X': '1001', 'Y': '1011',
  'Z': '1100', '_': '0011', '.': '1110', ',': '0101', '?': '1111',
}

def to_morse(s):
  ret = ""
  ln = []
  
  for i in s:
    ret += morse_code_dict[i]
    ln.append(len(morse_code_dict[i]))
  
  return [ret, ln]


def to_str(morse, ln):
  key = {}
  
  for k, v in morse_code_dict.items():
    key[v] = k
    
  ans = ""
  crt = 0
  
  for i in ln:
    ans += key[morse[crt:crt+i]]
    crt += i
  
  return ans


def solve():
  s = inp()
  
  morse, ln = to_morse(s)
  ln = ln[::-1]
  
  ans = to_str(morse, ln)

  p(ans)

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    p(end = f"{t}: ")
    ret = solve()
