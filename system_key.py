import os
from configparser import ConfigParser

import constants


class SystemKeys(object):

    def __init__(self):
        self.path_file = constants.DIRECTORY_SYSTEM + constants.NAME_FILE_KEY

    def create_file_key(self, path=constants.DIRECTORY_SYSTEM):
        try:
            f = open(self.path_file, 'w')
            f.close()
        except IOError:
            os.makedirs(path, exist_ok=True)
            f = open(self.path_file, 'w')
            f.close()

    def write_default_text_keys(self):
        config = ConfigParser()
        config.read(self.file)

        config.add_section('public_key')
        config.add_section('private_key')

        config.set('public_key', 'key', '')
        config.set('private_key', 'key', '')

        with open(self.file, 'w') as configfile:
            config.write(configfile)

    def set_public_key(self, key=''):
        self.__set_key('public_key', key)

    def set_private_key(self, key=''):
        self.__set_key('private_key', key)

    def get_public_key(self):
        return self.__get_key('public_key')

    def get_private_key(self):
        return self.__get_key('private_key')

    def __set_key(self, section='public_key', key=''):
        config = ConfigParser()
        config.read(self.path_file)

        config.set(section, 'key', key)

        with open(self.path_file, 'w') as configfile:
            config.write(configfile)

    def __get_key(self, section='public_key', name_key='key'):
        config = ConfigParser()
        config.read(self.path_file)

        return config.get(section, name_key)
