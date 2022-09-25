'''
[25238: 가희와 방어율 무시](https://www.acmicpc.net/problem/25238)

Tier: Bronze 5
Category: 구현
'''


def solution(a: int, b: int) -> int:
    '''몬스터의 방어율과 유저의 방무를 고려했을 때, 유저가 몬스터에게 데미지를 줄 수 있는지를 반환함.

    Args:
        a (int): 몬스터의 방어율
        b (int): 유저의 방무

    Returns:
        int: 0 또는 1로 결과값을 반환함.
    '''
    return int(a - (a * b / 100) < 100)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solution(a, b))
