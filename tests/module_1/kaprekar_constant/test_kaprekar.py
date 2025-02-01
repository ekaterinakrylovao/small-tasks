"""
Тесты для модуля kaprekar.
"""

import pytest
from module_1.kaprekar_constant.kaprekar import count_k


def test_count_k():
    assert count_k(3524) == 3
    assert count_k(6621) == 5
    assert count_k(6554) == 4
    assert count_k(1234) == 3
    assert count_k(6174) == 0  # Уже 6174, шагов не нужно


def test_invalid_input():
    with pytest.raises(ValueError, match="Число должно быть четырёхзначным"):
        count_k(999)  # Меньше 4 цифр

    with pytest.raises(ValueError, match="Число должно быть четырёхзначным"):
        count_k(10000)  # Больше 4 цифр

    with pytest.raises(ValueError, match="Число не должно состоять из одинаковых цифр"):
        count_k(1111)  # Все цифры одинаковые
