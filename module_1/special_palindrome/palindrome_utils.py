"""
Модуль содержит функцию для проверки, является ли число особым палиндромом
или его потомок (до длины > 1) является палиндромом.
"""


def is_palindrome_descendant(n: int) -> bool:
    """
    Проверяет, является ли число палиндромом или один из его потомков является палиндромом.

    Потомок создается путём суммирования каждой пары соседних цифр.

    Пример:
    - is_palindrome_descendant(11211230) -> True (11211230 -> 2333 -> 56 -> 11)
    - is_palindrome_descendant(13001120) -> True (13001120 -> 4022 -> 44)
    - is_palindrome_descendant(23336014) -> True (23336014 -> 5665)
    - is_palindrome_descendant(11) -> True

    :param n: Исходное число.
    :return: True, если число или его потомок является палиндромом, иначе False.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Число должно быть положительным целым")

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    num_str = str(n)
    while len(num_str) > 1:
        if is_palindrome(num_str):
            return True

        if len(num_str) % 2 != 0:
            break  # Если нечетное количество цифр, дальнейшее преобразование невозможно

        num_str = "".join(str(int(num_str[i]) + int(num_str[i + 1])) for i in range(0, len(num_str), 2))

    return False
