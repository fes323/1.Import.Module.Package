from application.salary import calculate_salary


from application.db.people import get_employees


from bs4 import BeautifulSoup


import requests
import os


# print(bs4.__version__) --- проверка версии

def delete_templates_dir():
    try:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'parse_html_templates')
        os.remove(path)
    except TypeError as Error:
        print(Error)


def create_templates_dir():
    try:
        os.mkdir('parse_html_templates')
    except TypeError as Error:
        print(Error)


def html_parser():
    url = input('Вставьте ссылку сайта:\n')

    user_input_elementOrFull = input('Хотите найти все ссылки с сайта? Введите: 1\n'
                                     'Хотите получить файл целиком? Введите: 2\n ')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #Получение HTML шаблона (просто тестил работу)
    if user_input_elementOrFull == '2':

        #создание файла
        try:
            parse_file = open('./parse_html_templates/index.html', 'w+', encoding='utf-8')
            parse_file.close()
        except TypeError as Error:
            print(Error)

        #заполнение файла
        try:
            parse_file = open('./parse_html_templates/index.html', 'a+', encoding='utf-8')
            parse_file.write(soup.prettify())
            parse_file.close()
        except TypeError as Error:
            print(Error)

    #Получение всех ссылок
    if user_input_elementOrFull == '1':
        try:
            for a in soup.find_all('a', href=True):
                parse_file = open('./parse_html_templates/url_or_phone.html', 'a+', encoding='utf-8')
                parse_file.write('\nНайдена ссылка:')
                parse_file.write(a['href'])
                parse_file.close()
        except TypeError as Error:
            print(Error)


def main():
    while True:

        var_dell = 'dell'
        var_dell_file = 'dell file'
        var_create = 'create'
        var_parse = 'parse'
        var_exit = 'exit'

        print('Список команд:\n'
              '1. dell - удалить папку с шаблонами\n'
              '2. create - создать папку с шаблонами\n'
              '3. parse - скачать шаблон сайта\n'
              '4. exit - прекратить выполнение программы\n'
              '5. dell file - удалить index.html\n')

        user_input = input('Введите команду:\n')

        if user_input == var_dell:
            try:
                delete_templates_dir()
                print('\nУспешное выполнение. Директория удалена.\n')
            except TypeError as Error:
                print(Error)

        if user_input == var_dell_file:
            try:
                os.remove('./parse_html_templates/index.html')
                print('\nУспешное выполнение. Файл удален.\n')
            except TypeError as Error:
                print(Error)

        if user_input == var_create:
            try:
                create_templates_dir()
                print('\nУспешное выполнение. Директория создана.\n')
            except TypeError as Error:
                print(Error)

        if user_input == var_parse:
            try:
                html_parser()
                print('\nУспешное выполнение. Файл создан.\n')
            except TypeError as Error:
                print(Error)

        if user_input == var_exit:
            print('\nЗавершение работы\n')
            break


if __name__ == '__main__':
    #main()
    calculate_salary()
    get_employees()