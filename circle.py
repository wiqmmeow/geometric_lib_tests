import math


def area(r):
    """Рассчитывает площадь круга.

    Используется формула S = pi * r^2, где число pi берётся из модуля math.

    Args:
        r: радиус круга (число, больше нуля).

    Returns:
        Площадь круга.

    Example:
        >>> circle.area(4)
        50.26548245743669
    """
    return math.pi * r * r


def perimeter(r):
    """Рассчитывает длину окружности.

    Используется формула P = 2 * pi * r, где число pi берётся из модуля math.

    Args:
        r: радиус круга (число, больше нуля).

    Returns:
        Длина окружности.

    Example:
        >>> circle.perimeter(4)
        25.132741228718345
    """
    return 2 * math.pi * r
