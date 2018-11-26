import json #для работы с json
import os #для работы с файловой системой
import hashlib # библиотека для хэширования

NAME_DIR = '/blockchain/'

'''
Функция получения пути к блокам сети
$return: строку, представляющую из себя путь до дирректории
'''
def get_blockchain_dir():
    return os.curdir + NAME_DIR

'''
Функция проверяет, является ли массив пустым
'''
def arrIsEmpty(arr):
    return ((arr is None) or (len(arr) == 0))

'''
Функция получения хэша файла
$Param: имя файла
$return: хэш файла
'''
def get_hash(filename):
    blockchain_dir = get_blockchain_dir()
    file = open(blockchain_dir + filename, 'rb').read();

    return hashlib.sha3_256(file).hexdigest();

'''
Функция сортирует имена файлов
$Param: путь
$return: отсортированный список
'''
def get_list_files(path):
    files = os.listdir(path)
    files = sorted([int(i) for i in files])

    return files

'''
Функция проверки целостности блокчейна
'''
def check_integrity():
    blockchain_dir = get_blockchain_dir()
    files = get_list_files(blockchain_dir)

    for file in files[1:]: #с первого элемента массива
        h = json.load(open(blockchain_dir + str(file)))['hash'] #получить свойство hash json фвйла

        prev_file = str(file - 1)

        actual_hash = get_hash(prev_file) #получаем хэш прошлого блока

        if h == actual_hash:
            res = 'OK'
        else:
            res = 'Corrupted'

        print('block {} is: {}'.format(prev_file, res))


'''
Запись нового блока в директорию blockchain
Файлы хроним в формате json
Имна файлов - номера блоков без расширения
$Params: имя человека, сумма, кому перечисление, хэш прошлого блока
'''
def write_block(name, amount, to, hash=''):

    blockchain_dir = get_blockchain_dir() # Получаем путь к папке с блоками
    files = get_list_files(blockchain_dir)

    if arrIsEmpty(files): # если нет блоков, создаем под номером 0
        filename = '0'
    else:
        prev_file = files[-1]  # получили номер последнего файла

        filename = str(prev_file + 1)

        hash = get_hash(str(prev_file)) # получаем хэш предыдущего блока

    data = {'name': name,
            'amount': amount,
            'to': to,
            'hash': hash}

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        '''
        Это запиь в файл в формате JSON
        indent - отступы (чтоб было не в одну линию) //потом можно убрать для уменьшения размера
        ensure_ascii - поддержка ASCII символов
        '''


def main():
    write_block('Serj', 10, 'Kiril')
    write_block('Alex', 30, 'Serj')
    write_block('No name', 2, 'Kiril')
    write_block('Serj', 102, 'Kiril')
    check_integrity()

if __name__ == '__main__':
    main()