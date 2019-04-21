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
    def __check_network(self):
        users = self.__json__.get_json(Const.PATH_TO_LIST_USERS)

        if not users:
            return

        count_action_users = 0

        for id_user, data_user in users.items():
            message = self.__network__.create_message("lerner_check-active", {})
            success = self.__network__.send(data_user["ip"], Const.PORT_USER, message)

            if success:
                count_action_users += 1

        print('action users: ' + str(count_action_users))

    def __get_message(self, message):
        """Метод обработки всех пришедших сообщений"""
        self._action(message)
