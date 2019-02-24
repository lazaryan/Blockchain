import os

from files import Files

import constants


class Temporary(Files):
    """Класс для с системными временными файлами"""
    def __init__(self):
        super().__init__()

        self.__path = constants.DIRECTORY_TMP

        self._create_tmp_files()

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
