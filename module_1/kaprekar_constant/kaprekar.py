"""
Модуль содержит функцию Капрекара.
"""


def count_k(n: int, steps: int = 0) -> int:
    """
    Рекурсивно вычисляет количество шагов до достижения числа 6174
    согласно процессу Капрекара.

    :param n: Четырёхзначное число с разными цифрами
    :param steps: Текущий счетчик шагов (по умолчанию 0)
    :return: Количество шагов до достижения 6174
    :raises ValueError: Если число не четырёхзначное или содержит одинаковые цифры
    """
    if not (1000 <= n <= 9999):
        raise ValueError("Число должно быть четырёхзначным (1000-9999).")

    digits = set(str(n))
    if len(digits) == 1:
        raise ValueError("Число не должно состоять из одинаковых цифр.")

    if n == 6174:
        return steps

    str_n = f"{n:04d}"  # Обеспечиваем сохранение ведущих нулей
    ascending = int("".join(sorted(str_n)))
    descending = int("".join(sorted(str_n, reverse=True)))

    return count_k(descending - ascending, steps + 1)
