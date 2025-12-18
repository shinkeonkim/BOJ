def is_right_parenthesis(s):
    stk = 0

    for c in s:
      if c == '(':
        stk += 1
        continue

      if stk == 0:
        return False

      stk -= 1

      if stk < 0:
        return False

    return stk == 0


def solve():
  s = input()
  return is_right_parenthesis(s)


if __name__ == "__main__":
  tc = int(input())
  for t in range(1, tc+1):
    ret = solve()
    print("YES" if ret else "NO")

