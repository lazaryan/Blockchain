from essense.secondary.fs.json_files import JsonFiles
from essense.action.learner import ActionLearner
from essense.secondary.network import Network
from essense.secondary.decorators import *
from essense.const import Const


class Learner(ActionLearner):
    """
    Класс доверенного узла
    """
    __PAUSE_CHECK_USERS__ = 10  # Задержка проверки сети на наличие пользователей (в секундах)

    __network__ = Network()  # Свойство для работы с сетью
    __json__ = JsonFiles()  # Свойство для работы с json файлами

    def __init__(self, start=False):
        super().__init__()
        self.__clear_start_files()

        if start:
            self.start()

    def start(self):
        """Метод запуска основных функций learner"""
        self.server()
        self.check_network()

    @thread
    def server(self):
        """Запуск сервера на прослушку сети"""
        self.__network__.server(Const.PORT_LEARNER, self.__get_message, Const.LISTEN_LEARNER)

    @thread
    def check_network(self):
        """Метод проверки всех узлов на наличие в сети.
        Запускается в отдельном потоке и в бесконечном цикле запускает метод проверки
        Метод проверки запускается с паузой, останавливая данный поток
        """
        print('CHECK NETWORK START...')
        while True:
            self.__check_network()

    @pause(__PAUSE_CHECK_USERS__)
    @thread
    def __check_network(self):
        users = self.__json__.get_json(Const.PATH_TO_LIST_USERS)
        data = self.__json__.get_json(Const.PATH_TO_DATA)

        if not users:
            return

        body = {}

        if data:
            if data.get('id'):
                body["id"] = data["id"]

        dis_active_users = []
        active_users = {}

        for id_user, data_user in users.items():
            message = self.__network__.create_message("lerner_check-active", body)
            success = self.__network__.send(data_user["ip"], Const.PORT_USER, message)

            if success:
                active_users[id_user] = data_user
            else:
                dis_active_users.append(id_user)

        print('action users: ' + str(len(active_users)))

        change = self.change_action_users(active_users, dis_active_users)
        print(change)

    def __get_message(self, message):
        """Метод обработки всех пришедших сообщений"""
        self._action(message)

    def __clear_start_files(self):
        """Очистка файлов и дерикторий, оставшихся после последнего запуска"""
        self.__json__.delete_file(Const.PATH_TO_LIST_USERS_ACTION)
