'''
[24603: Scaling Recipe](https://www.acmicpc.net/problem/24603)

Tier: Bronze 3
Category: 구현
'''


def solution(x: int, y: int, gredients: list) -> list:
    '''gradidents를 받아 y/x배 scale up 하여 반환합니다.

    Args:
        x (int): x
        y (int): y
        gredients (list): 재료 개수

    Returns:
        list: y/x배 scale up된 배열
    '''

    return [gredient * y // x for gredient in gredients]


if __name__ == '__main__':
    n, x, y = map(int, input().split())
    gradients = [int(input()) for _ in range(n)]

    answer = solution(x, y, gradients)

    print('\n'.join(map(str, answer)))
