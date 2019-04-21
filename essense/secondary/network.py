import socket
import json
import urllib.request
import urllib.error
from essense.secondary.decorators import *


class Network(object):
    """
    Класс для работы с сетью
    """
    __PORT__ = 9000  # Port на котром работает сервер (дефолтное значение)
    __LISTEN__ = 10  # Сколько пользователей одновременно могут подключиться (дефолтное значение)

    @staticmethod
    def __callback_server(message):
        """Дефолтный метод обработки сообщения на сервер"""
        print(message)

    @thread
    def server(self, port=__PORT__, callback=__callback_server, listener=__LISTEN__):
        """
        Метод мониторинга сети на наличие запросов
        Функция работает в отдельном потоке
        :param port: <int> Порт, на котором работает сервер
        :param callback: <func> Функция, которая будет обрабатывать пришедшее сообщение
        :param listener: <int> Сколько пользователей одновременно могут подключиться
        :return: <func> функцию, которая в бесконечном цикле будет прослушивать сеть
        """
        print("SERVER START...")
        sock = socket.socket()
        sock.bind(('', port))

        while True:
            sock.listen(listener)
            conn, addr = sock.accept()
            message = conn.recv(1023).decode()

            if callback:
                callback(message)

    @staticmethod
    def send(ip, port, message):
        """
        Метод отправки сообщения другому пользователю сети
        :param ip: <str> ip адресс пользователя, которому отправляется сообщение
        :param port: <int> Порт, на котором он слушает запросы
        :param message: <str> Передоваемое сообщение
        :return: <bool> Успешность операции
        """
        sock = socket.socket()
        try:
            sock.connect((ip, port))
        except TimeoutError:
            return False
        except ConnectionRefusedError:
            return False

        sock.send(message)
        sock.close()

        return True

    def create_message(self, type_message, data):
        """
        Метод для создания тела сообщение другимпользователям
        :param type_message: <str> Тип передоваемого сообщения
        :param data: <all> Тело сообщения. может быть любым типом данных, который используется в json стандарте
        :return: <str> Строковое представление объекта
        """
        message = {
            "header": {
                "type": type_message,
                "ip": self.get_local_ip(),
                "ip_global": self.get_global_ip()
            },
            "data": data
        }

        return json.dumps(message)

    def get_port(self):
        """Метод получения порта, на котором работает сеть"""
        return self.__PORT__

    @staticmethod
    def get_global_ip():
        """
        Метод получения белого ip адресса (глобального)
        Работает по принципу отправки запроса на сервер, предоставляющий такую возможность
        :return: <str> ip адресс пользователя в интернете
        """
        try:
            return urllib.request.urlopen('http://ip-address.ru/show').read().decode('utf-8')
        except urllib.error.URLError:
            return ''

    @staticmethod
    def get_local_ip():
        """
        Метод получения серого ip адресса (локальная сеть)
        :return: локальный ip адресс
        """
        return socket.gethostbyname(socket.getfqdn())
