"""
[24408: Mult](https://www.acmicpc.net/problem/24408)

Tier: Bronze 3
Category: 구현
"""


def solution(numbers: list) -> list:
    """ Return numbers that shout of Mult!

    Args:
        numbers (list): numbers

    Returns:
        list: numbers that shout of Mult!
    """
    answer = []
    crt = -1

    for number in numbers:
        if crt == -1:
            crt = number
        elif number % crt == 0:
            answer.append(number)
            crt = -1

    return answer


if __name__ == '__main__':
    n = int(input())
    numbers = [int(input()) for i in range(n)]

    print('\n'.join(map(str, solution(numbers))))
