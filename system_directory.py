from keys import Keys
from temporary import Temporary


class SystemDirectory(object):
    def __init__(self):
        self.__keys = Keys()
        self.__temporary = Temporary()

    """Методы работы с ключами"""
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

    """Методы работы с временными файлами"""
    def set_action_user(self, id_user='', data=''):
        """Метод добавления активного пользователя"""
        self.__temporary.add_action_user(id_user, data)

    def get_data_action_user(self, id_user=''):
        """Метод получения информации об активном пользователе"""
        return self.__temporary.get_data_action_user(id_user)

    def delete_action_user(self, id_user=''):
        """Метод удаления пользователя из списка активных"""
        self.__temporary.delete_action_user(id_user)

    def set_proposal_user(self, id_user='', data=''):
        """Метод добавления активного пользователя со статусом Proposer"""
        self.__temporary.add_proposal_user(id_user, data)

    def get_data_proposal_user(self, id_user=''):
        """Метод получения информации о пользователе со статусом Proposer"""
        return self.__temporary.get_data_proposal_user(id_user)

    def delete_proposal_user(self, id_user=''):
        """Метод удаления пользователя из списка узлов со статусом Proposer"""
        self.__temporary.delete_proposal_user(id_user)
