import creation as cr
import logger as lg


print('\nВас приветствует телефонная книга')


def ls_menu():
    while True:
        print('\nМЕНЮ')
        print('1. Показать все записи.')
        print('2. Найти номер по фамилии.')
        print('3. Найти номер по имени.')
        print('4. Поиск по номеру телефона.')
        print('5. Добавить новую запись.')
        print('6. Изменить существующую запись.')
        print('7. Удалить запись.')
        print('8. Закрыть программу.\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            lg.logging.info('Пользователь выбрал номер позиции 1')
            x = cr.retrive()
            if len(x) != 0:
                for row in x:
                    print(row[0], row[1], row[2], row[3], row[4])
            else:
                print('Контакты не найдены')
                

        elif n == 2:
            lg.logging.info('Пользователь выбрал номер позиции 2')
            search = input('Введите фамилию: ')
            lg.logging.info('Пользователь ввел: {search}')
            print(cr.retrive(surname=search))

        elif n == 3:
            lg.logging.info('Пользователь выбрал номер позиции 3')
            search = input('Введите имя: ')
            lg.logging.info('Пользователь ввел: {search}')
            print(cr.retrive(name=search))

        elif n == 4:
            lg.logging.info('Пользователь выбрал номер позиции 4')
            search = input('Введите номер  телефона: ')
            lg.logging.info('Пользователь ввел: {search}')
            print(cr.retrive(number=search))

        elif n == 5:
            lg.logging.info('Пользователь выбрал номер позиции 5')
            name = input('Введите имя: ')
            lg.logging.info('Пользователь ввел: {name}')
            surname = input('Введите фамилию: ')
            lg.logging.info('Пользователь ввел: {surname}')
            number = input('Введите номер телефона: ')
            lg.logging.info('Пользователь ввел: {number}')
            email = input('Введите электронную почту: ')
            lg.logging.info('Пользователь ввел: {email}')
            cr.create(name, surname, number, email)

        elif n == 6:
            lg.logging.info('Пользователь выбрал номер позиции 6')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 1:
                lg.logging.info('Пользователь выбрал номер позиции 6.1')
                search = input('Введите фамилию: ')
                lg.logging.info('Пользователь ввел: {search}')
                cr.retrive(surname=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('Пользователь ввел: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            elif change == 2:
                lg.logging.info('Пользователь выбрал номер позиции 6.2')
                search = input('Введите имя: ')
                lg.logging.info('Пользователь ввел: {search}')
                cr.retrive(name=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('Пользователь ввел: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('Пользователь ввел:{new_number}')
                cr.update(id=user_id, new_number=new_number)

            elif change == 3:
                lg.logging.info('Пользователь выбрал номер позиции 6.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('User entered: {search}')
                cr.retrive(number=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('Пользователь ввел: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('Пользователь ввел: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            else:
                lg.logging.info('Пользователь ввел недопустимое значение меню')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 7:
            lg.logging.info('Пользователь выбрал номер позиции 7')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                lg.logging.info('Пользователь выбрал номер позиции 7.1')
                search = input('Введите фамилию: ')
                lg.logging.info('Пользователь ввел: {search}')
                print(cr.retrive(surname=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('Пользователь ввел: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('Пользователь выбрал номер позиции 7.2')
                search = input('Введите имя: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(name=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('Пользователь ввел: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 3:
                lg.logging.info('Пользователь выбрал номер позиции 7.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('Пользователь ввел: {search}')
                print(cr.retrive(number=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('Пользователь ввел: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                cr.delete(id=user_id)

            else:
                lg.logging.info('Пользователь ввел недопустимое значение меню:')
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 8:
            lg.logging.info('End')
            print('Спасибо за работу!')
            break

        else:
            lg.logging.info('Пользователь ввел недопустимое значение меню: {n}')
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('Пользователь ввел недопустимое значение меню: {arg}')
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)