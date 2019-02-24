from keys import Keys
from temporary import Temporary


class SystemDirectory(object):
    def __init__(self):
        self.__keys = Keys()
        self.__temporary = Temporary()

    def set_public_key(self, key=''):
        """Метод внесения публичного ключа"""
        self.__keys.set_public_key(key)

    def get_public_key(self):
        """Метод получения публичного ключа"""
        return self.__keys.get_public_key()

    def set_private_key(self, key=''):
        """Метод внесения приватного ключа"""
        self.__keys.set_private_key(key)

    def get_private_key(self):
        """Метод получения приватного ключа"""
        return self.__keys.get_private_key()
