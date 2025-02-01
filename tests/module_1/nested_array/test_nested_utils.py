"""
Тесты для модуля nested_utils.
"""

import pytest
from module_1.nested_array.nested_utils import is_nestable


@pytest.mark.parametrize("a1, a2, expected", [
    ([1, 2, 3, 4], [0, 6], True),
    ([3, 1], [4, 0], True),
    ([9, 9, 8], [8, 9], False),
    ([1, 2, 3, 4], [2, 3], False),
    ([5], [4, 6], True),
    ([5], [5], False),  # граничный случай
    ([5, 10], [4, 11], True),
    ([5, 10], [5, 10], False),  # границы равны
])
def test_is_nestable(a1, a2, expected):
    assert is_nestable(a1, a2) == expected


def test_is_nestable_raises():
    with pytest.raises(ValueError, match="Оба массива должны содержать хотя бы один элемент"):
        is_nestable([], [1, 2, 3])

    with pytest.raises(ValueError, match="Оба массива должны содержать хотя бы один элемент"):
        is_nestable([1, 2, 3], [])
