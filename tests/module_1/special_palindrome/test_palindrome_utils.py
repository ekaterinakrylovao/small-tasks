"""
Тесты для модуля palindrome_utils.
"""

import pytest
from module_1.special_palindrome.palindrome_utils import is_palindrome_descendant


def test_is_palindrome_descendant():
    assert is_palindrome_descendant(11211230) is True  # 11211230 -> 2333 -> 56 -> 11
    assert is_palindrome_descendant(13001120) is True  # 13001120 -> 4022 -> 44
    assert is_palindrome_descendant(23336014) is True  # 23336014 -> 5665
    assert is_palindrome_descendant(11) is True  # Уже палиндром
    assert is_palindrome_descendant(123456) is False  # Не становится палиндромом
    assert is_palindrome_descendant(1) is False  # Было ограничение на длину > 1

    with pytest.raises(ValueError):
        is_palindrome_descendant(-11211230)  # Нельзя отрицательное число
    with pytest.raises(ValueError):
        is_palindrome_descendant("123321")  # Строка вместо числа
