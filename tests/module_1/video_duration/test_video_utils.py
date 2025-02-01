"""
Тесты для модуля video_utils.
"""

import pytest
from module_1.video_duration.video_utils import VideoDurationConverter


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("01:00", 60),
        ("13:56", 836),
        ("10:60", -1),  # Некорректный формат
        ("999:59", 59999),  # Корректный формат с большим числом минут
        ("00:00", 0),
        ("00:59", 59),
        ("01:01", 61),
        ("-01:30", -1),  # Отрицательные числа невалидны
        ("1:5", -1),  # Должно быть ровно 2 цифры в секундах
        ("abc:def", -1),  # Некорректные символы
        ("12:34:56", -1),  # Лишний блок
        ("12:345", -1),  # Лишние цифры в секундах
        ("", -1),  # Пустая строка
        (None, -1),  # None вместо строки
        (123, -1),  # Неверный тип данных
    ],
)
def test_minutes_to_seconds(input_str, expected):
    assert VideoDurationConverter.minutes_to_seconds(input_str) == expected
