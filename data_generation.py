import random
import csv
import logger as lg
from transliterate import slugify

# ls_name = ['Svetlana', 'Olga', 'Anton', 'Anna', 'Inna', 'Natalia',
#             'Victor', 'Sergey', 'Aleksey', 'Mikhail', 'Igor', 'Dmitry']
# ls_surname = ['Kovalenko', 'Stepanenko', 'Galich', 'Soshenko', 'Dmitriyenko', 
#                 'Chernykh', 'Boyko', 'Paganini', 'Globa', 'Zima', 'Morgun', 'Zima']
# ls_e_mail = ['@gmail.com', '@yandex.ru', '@mail.ru']


ls_name = ['Светлана', 'Ольга', 'Антон', 'Анна', 'Инна', 'Наталья', 
           'Виктор', 'Сергей', 'Алексей', 'Михаил', 'Игорь', 'Дмитрий']
ls_surname = ['Коваленко', 'Степаненко', 'Галич', 'Сошенко', 'Дмитриенко',
              'Черных', 'Бойко', 'Паганини', 'Глоба', 'Зима', 'Моргун', 'Зима']
ls_e_mail = ['@gmail.com', '@yandex.ru', '@mail.ru']


def list_of_numbers():
    randomListPhone = random.randint(79000000000, 80000000000)
    return str(randomListPhone)



def string_creation():
    s = ""
    a = random.choice(ls_name)
    b = random.choice(ls_surname)
    c = random.choice(ls_e_mail)
    email = slugify(a) + '.' + slugify(b) + c
    s = s + a + ',' + b + ',' + list_of_numbers() + ',' + email
    return s


def start():
    file = open('base_phone.csv', 'w', encoding='utf-8')
    newrecord = "ID,Name,Surname,PhoneNumber,Email\n"
    file.writelines(newrecord)

    for i in range(30):
        a = f'{str(i + 1)},{string_creation()}\n'
        file.write(a)
    file.close()


# start()