import os

from json_files import JsonFiles

import constants


class Temporary(JsonFiles):
    """Класс для с системными временными файлами"""
    def __init__(self):
        super().__init__()

        self.__path = constants.DIRECTORY_TMP

        self.__action_users = self.__get_path_to_file(self.__path, constants.NAME_FILE_ACTION_USER)
        self.__proposal_users = self.__get_path_to_file(self.__path, constants.NAME_FILE_PROPOSALS_USER)

        self._create_tmp_files()

    def add_action_user(self, id_user='', data=''):
        """Метод добавления вошедшего участника в список активных узлов

        :param id_user: Идентификатор пользователя (его публичный ключ)
        :param data: Необходимая информация о пользователе
        :return: Ничего не возвращает
        """
        self._set_property(self.__action_users, id_user, data)

    def get_data_action_user(self, id_user):
        """Метод получения информации о пользователе"""
        return self._get_property(self.__action_users, id_user)

    def delete_action_user(self, id_user):
        """Метод удаления пользователя из списка активных"""
        self._del_property(self.__action_users, id_user)

    def add_proposal_user(self, id_user='', data=''):
        """Метод добавления вошедшего участника в список активных узлов со статусом Proposer

        :param id_user: Идентификатор пользователя (его публичный ключ)
        :param data: Необходимая информация о пользователе
        :return: Ничего не возвращает
        """
        self._set_property(self.__proposal_users, id_user, data)

    def get_data_proposal_user(self, id_user):
        """Метод получения информации о пользователе"""
        return self._get_property(self.__proposal_users, id_user)

    def delete_proposal_user(self, id_user):
        """Метод удаления пользователя из списка узлов со статусом Proposer"""
        self._del_property(self.__proposal_users, id_user)

    def _create_tmp_files(self):
        """Метод для создания временных файлов

        Создаются файлы для записи активных участников сети
        И для участников сети со статусом Proposer (для быстрого доступа)

        :return: Ничего не возвращает
        """
        action_users = self.__get_path_to_file(self.__path, constants.NAME_FILE_ACTION_USER)
        proposal_users = self.__get_path_to_file(self.__path, constants.NAME_FILE_PROPOSALS_USER)

        self._create_file(action_users)
        self._create_file(proposal_users)

    @staticmethod
    def __get_path_to_file(path='./', name_file=''):
        """Метод для склеивания директории и имени файла"""
        return os.path.join(path, name_file)
