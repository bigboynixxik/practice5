# Программа, реализующую решение задачи покрытия множества с помощью жадных алгоритмов.
Жадный алгоритм:
* выбрать оператора, покрывающего наибольшее количество регионов, и еще не входящих в покрытие.
* повторять, пока остаются непокрытые элементы множестваю
### Функции использующиеся в программе
* [x] **Первая** _будет обрабатывать ввод пользователя и возвращать словарь с операторами_.
* [x] **Вторая** _будет обрабатывать ввод пользователя и возвращать множество регионов_.
* [x] **Третья** _будет обрабатывать данные, которые мы получим с помощью первой и второй функции, и возвращать ответ_.
* [ ] **Четвёртая** _запускает меню. В данной функции обрабатывается поведение программы с помощью введённых пользователем данных_. 

### Основная функция и точка входа в программу
```
def menu() -> None:
    '''
    Запускает меню. В данной функции обрабатывается поведение программы.
    У пользователя появляется выбор того, что бы он хотел сделать.

    Return:
        None
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
    reg_dict()
    menu()
```
Вы можете почитать про сиракузскую последовательность [тут]([https://ru.wikipedia.org/wiki/Гипотеза_Коллатца](https://discopal.ispras.ru/img_auth.php/8/82/Greedy-covering.beam.pdf)https://discopal.ispras.ru/img_auth.php/8/82/Greedy-covering.beam.pdf)
![](http://images.myshared.ru/62/1347752/slide_16.jpg)
