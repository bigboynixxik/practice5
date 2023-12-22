'''
Задание №5 ОП практическая работа №3
Программа, реализующую решение задачи покрытия
множества с помощью жадных алгоритмов.
'''


def solution(region: set, diction: dict) -> str:
    '''
    Функция возвращает ответ на задауч. (Искоmые регионы покрытия)
    :param diction: (int) - Первый аргумент
    :param region: (dict) - Второй аргумент
    :return ans(list) - ответ на задачу:
    :return st(str) - ответа нет(:
    '''
    ans = []
    st = ''
    while region:
        list_of_tuples = []

        for key, value in diction.items():
            list_of_tuples.append((key, value & region))

        if all(time_try[1] == set() for time_try in list_of_tuples):
            st = 'Данный регион не может покрыть ни один из операторов =('
            break

        list_of_tuples.sort(key=lambda x: len(x[1]), reverse=True)
        region -= list_of_tuples[0][1]
        ans.append(list_of_tuples[0][0])

        del diction[list_of_tuples[0][0]]

    if st != '':
        return st
    return ans


def reg_dict():
    '''
    Обработка операторов связи
    :return dictionary(dict) - словарь с операторами связи и их регионами покрытия:
    '''
    dictionary = {}

    try:
        length = int(input("Введите количество операторов связи: "))
    except ValueError:
        print('Ошибка ввода данных. Пожалуйста, введите корректные данные')
        length = int(input("Введите количество операторов связи: "))

    print('Введите данные в словарь. Формат: "key: value1 value2 .. value_n"')
    for _ in range(length):
        try:
            key, value = input().split(': ')
            value = value.split()
        except ValueError:
            print('Ошибка ввода данных. Введите данные в словарь.'
                  ' Формат: "key: value1 value2 .. value_n"')
            key, value = input().split(': ')
            value = value.split()

        try:
            value = list(map(int, value))
        except ValueError:
            print('Ошибка ввода данных. Введите данные в словарь.'
                  ' Формат: "key: value1 value2 .. value_n"')
            key, value = input().split(': ')
            value = value.split()
            value = list(map(int, value))

        dictionary[key] = set()
        dictionary[key].update(value)
    return dictionary


def reg_regions():
    '''
    Обработка необходимых для покрытия регионов
    :return need_regions(set) - необходимые для  покрытия регионы:
    '''
    need_regions = set()
    try:
        regions = input('Введите необходимые для покрытия регионы.'
                        ' Формат: "value1 value2 .. value_n"\n').split()
    except ValueError:
        print('Ошибка ввода данных. Пожалуйста, введите корректные данные')
        regions = input('Введите необходимые для покрытия регионы.'
                        ' Формат: "value1 value2 .. value_n"\n').split()

    try:
        regions = list(map(int, regions))
    except ValueError:
        print('Ошибка ввода данных. Пожалуйста, введите корректные данные')
        regions = input('Введите необходимые для покрытия регионы.'
                        ' Формат: "value1 value2 .. value_n"\n').split()
        regions = list(map(int, regions))

    need_regions.update(regions)
    return need_regions


def menu():
    '''
    Запускает програmmу и создаёт её mеню.
    :return answer:
    '''
    count = 0
    while True:
        count += 1
        print(f'Меню выполнения программы № {count}:\n'
              'Если вы хотите завершить программу, введите "Close"\n'
              'Если вы хотите сначала ввести словарь с операторами'
              ' и их регионами покрытия, введите "1"\n'
              'Если вы хотите сначала ввести необходимые для покрытия регионы, введите "2"')

        command = input()

        if command == 'Close':
            break
        if command == '1':
            com1 = reg_dict()
            com2 = reg_regions()
            print(f'Ответ: {solution(com2, com1)}')
        if command == '2':
            print(f'Ответ: {solution(reg_regions(), reg_dict())}')
        else:
            com1 = reg_dict()
            com2 = reg_regions()
            print(f'Ответ: {solution(com2, com1)}')

if __name__ == '__main__':
    menu()