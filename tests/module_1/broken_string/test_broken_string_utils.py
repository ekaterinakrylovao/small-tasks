"""
Тесты для модуля broken_string_utils.
"""

import pytest
from module_1.broken_string.broken_string_utils import fix_string


@pytest.mark.parametrize("input_str, expected", [
    ("123456", "214365"),
    ("hTsii  s aimex dpus rtni.g", "This is a mixed up string."),
    ("badce", "abcde"),  # Нечётное количество символов в строке (как полследний пример, но короче)
    ("", ""),
    ("a", "a"),  # Одиночный символ остаётся на месте
    ("ab", "ba"),
    ("abcdefg", "badcfeg"),  # Последний символ остаётся на месте
])
def test_fix_string(input_str, expected):
    assert fix_string(input_str) == expected


def test_fix_string_invalid_type():
    with pytest.raises(TypeError, match="Входные данные должны быть строкой"):
        fix_string(12345)  # Передаём не строку
