import os
from directorys import Directory


class Files(Directory):
    """Класс для работы с файлами"""
    def __init__(self):
        super().__init__()

    def _create_file(self, path_to_file):
        """Создает файл и производит все необходимые проверки

        Метод создает при необходимости все необходимые директории
        Если файл уже существует - он не пересоздается

        :param path_to_file: Путь к файлу
        :return:
        """
        path = os.path.dirname(path_to_file)

        if os.path.exists(path):
            if not os.path.exists(path_to_file):
                open(path_to_file, 'w').close()
        else:
            self._create_directory(path)
            open(path_to_file, 'w').close()

    @staticmethod
    def _clear_file(path_to_file):
        """Очищает файл если он существует"""
        if not os.path.isfile(path_to_file):
            return ''

        open(path_to_file, 'w').close()

    @staticmethod
    def _delete_file(path_to_file=''):
        """Метод для удаления файла"""
        if os.path.isfile(path_to_file):
            os.remove(path_to_file)

    @staticmethod
    def _is_not_zero_file(path_to_file):
        """Проверяет файл на пустоту

        :param path_to_file: Путь к файлу
        :return: Возвращает Boolean значение
        """
        return os.path.isfile(path_to_file) and os.path.getsize(path_to_file) > 0
