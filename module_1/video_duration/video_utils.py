"""Модуль для работы с длительностью видео в формате mm:ss."""

import re


class VideoDurationConverter:
    """Класс для преобразования длительности видео из формата mm:ss в секунды."""

    @staticmethod
    def minutes_to_seconds(duration: str) -> int:
        """
        Преобразует строку формата mm:ss в количество секунд.

        :param duration: Длительность видео в формате mm:ss
        :return: Количество секунд или -1, если формат некорректен
        """
        if not isinstance(duration, str):
            return -1

        match = re.fullmatch(r"(\d+):(\d{2})", duration)
        if not match:
            return -1

        minutes, seconds = map(int, match.groups())

        if seconds >= 60:
            return -1

        return minutes * 60 + seconds
