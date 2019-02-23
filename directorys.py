import os
import errno


class Directory (object):
    """Класс для работы с директориями"""
    @staticmethod
    def _create_directory(path=''):
        """Создает директорию

        :param path: Путь к директории
        :return: Ничего не возвращает
        """
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as exception:
            if exception != errno.EEXIST:
                raise
