"""
[21983: Basalt Breakdown](https://www.acmicpc.net/problem/21983)

Tier: Bronze 3
Category: 구현
"""

from math import sqrt


def getPerimeterOfHexagon(area: int) -> int:
    """ 육각형의 넓이를 받아 모든 변의 길이의 합을 반환합니다.

    Args:
        area (int): 육각형의 넓이

    Returns:
        int: 모든 변 길이의 합
    """

    side = sqrt(2 * area / sqrt(27))  # 한변의 길이

    return side * 6


if __name__ == '__main__':
    print(getPerimeterOfHexagon(int(input())))
