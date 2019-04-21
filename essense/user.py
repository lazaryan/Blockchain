from essense.secondary.network import Network
from essense.secondary.decorators import *
from essense.const import Const


class User(object):
    __network__ = Network()

    @thread
    def server(self):
        """Запуск сервера на прослушку сети"""
        self.__network__.server(Const.PORT_USER, self.__get_message, Const.LISTEN_USER)

    def __get_message(self, message):
        pass
