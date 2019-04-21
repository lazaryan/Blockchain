from essense.secondary.fs.json_files import JsonFiles
from essense.const import Const


class ActionLearner(object):
    """Класс для выполнение сетевых запросов learner узла"""
    __json__ = JsonFiles()

    def _action(self, message):
        """
        Метод обработки запросов от других пользователей
        :param message: <obj> Объект запроса
        :return:
        """
        pass

    def change_action_users(self, action_users, dis_active_users):
        """
        Метод проверки изменения активности пользователей
        Если какой-то пользователь зашел в сеть или же наоборот вышел, то данные об этом обновляются
        :param action_users: <obj> json объект активных пользователей
        :param dis_active_users: <arr str> Массив id пользователей, которые сейчас не в сети
        :return: <obj> json объект, в котором указаны изменния активности
        """
        change = {"action": [], "dis_active": []}
        users = self.__json__.get_json(Const.PATH_TO_LIST_USERS_ACTION)

        for id_user, data in action_users.items():
            if not users.get(id_user):
                change["action"].append(id_user)
                users[id_user] = data

        for id_user in dis_active_users:
            if not users.get(id_user) is None:
                change["dis_active"].append(id_user)
                del users[id_user]

        if change["action"] or change["dis_active"]:
            self.__json__.set_json_in_file(Const.PATH_TO_LIST_USERS_ACTION, action_users)

        return change
