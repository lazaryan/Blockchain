import os

from json_files import JsonFiles
import constants


class Keys(JsonFiles):
    """Класс для работы с ключами приложения"""
    def __init__(self):
        super().__init__()

        self.SECTION_PUBLIC_KEYS = 'public_key'
        self.SECTION_PRIVATE_KEYS = 'private_key'

        path = constants.DIRECTORY_SYSTEM
        name_file = constants.NAME_FILE_KEY

        self.__path_to_file = os.path.join(path, name_file)

        self.write_default_keys_form()

    def write_default_keys_form(self):
        """Записывает в файл стартовую форму (секции и имена ключей)"""
        data = dict()
        data[self.SECTION_PUBLIC_KEYS] = {}
        data[self.SECTION_PUBLIC_KEYS]['key'] = ''

        data[self.SECTION_PRIVATE_KEYS] = {}
        data[self.SECTION_PRIVATE_KEYS]['key'] = ''

        if not os.path.isfile(self.__path_to_file):
            self.__create_file_key(data)

        if self._is_not_zero_file(self.__path_to_file):
            return ''

    def set_public_key(self, key=''):
        """Внесение публичного ключа

        Производится проверка на существование файла для записи
        При необходимости он создается, после чего записывается публичный ключ

        :param key: Публичный ключ
        :return: Ничего не возвращает
        """
        if not self._is_not_zero_file(self.__path_to_file):
            self.write_default_keys_form()

        self.__set_key(self.__path_to_file, self.SECTION_PUBLIC_KEYS, key)

    def set_private_key(self, key=''):
        """Внесение приватного ключа

        Производится проверка на существование файла для записи
        При необходимости он создается, после чего записывается приватный ключ

        :param key: Приватный ключ
        :return: Ничего не возвращает
        """
        if not self._is_not_zero_file(self.__path_to_file):
            self.write_default_keys_form()

        self.__set_key(self.__path_to_file, self.SECTION_PRIVATE_KEYS, key)

    def get_public_key(self):
        """Возвращает публичный ключ"""
        if not self._is_not_zero_file(self.__path_to_file):
            return ''

        return self.__get_key(self.__path_to_file, self.SECTION_PUBLIC_KEYS)

    def get_private_key(self):
        """Возвращает приватный ключ"""
        if not self._is_not_zero_file(self.__path_to_file):
            return ''

        return self.__get_key(self.__path_to_file, self.SECTION_PRIVATE_KEYS)

    def __create_file_key(self, data=()):
        """Создание файла для ключей"""
        self._create_file(self.__path_to_file, data)

    def __set_key(self, path_to_file, section, key):
        """Запись ключа

        :param path_to_file: Путь к файлу
        :param section: Имя секции (какой ключ: открытый, приватный или другой...)
        :param key: Значение ключа
        :return: Ничего не возвращает
        """
        data = self._get_json(path_to_file)

        try:
            data[section]['key'] = key
        except KeyError:
            data[section] = {}
            data[section]['key'] = key

        self._write_data(path_to_file, data)

    def __get_key(self, path_to_file, section, name_key='key'):
        """Возвращает сохраненный ключ

        :param path_to_file: Путь к файлу
        :param section: Имя секции, в которой хранится ключ
        :param name_key: Имя ключа
        :return: Ключ
        """
        data = self._get_json(path_to_file)

        try:
            return data[section][name_key]
        except KeyError:
            return ''
