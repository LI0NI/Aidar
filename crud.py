import json
from json.decoder import JSONDecodeError
from settings import FILE
from datetime import datetime
import shelve


def get_all_data():
    with open(FILE) as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []


def create_data():
    id_ = datetime.now().strftime('%H%M%S')
    data = {
        'id': id_,
        'title': input('Введите название '),
        'price': int(input('Введите цену ')),
        'description': input('Введие описание '),
        'data_created': datetime.now().strftime('%d.%m.%Y %H:%M'),
        'status': input('Статус товара продано/продается: ')
    }
    json_data: list = get_all_data()
    json_data.append(data)
    with open(FILE, 'w') as f:
        json.dump(json_data, f, indent=4)


def get_data_by_id():
    id_ = input('Введите id ')
    for obj in get_all_data():
        if obj['id'] == id_:
            return obj
    return 'Not found'



def delete_data():
    id_ = input('Введите id ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            data.remove(obj)
            break
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=4)


def update():
    id_ = input('Введите id: ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            obj['title'] = input('Введите название: ')
            obj['price'] = int(input('Введите цену: '))
            obj['description'] = input('Введите описание: ')
            obj['data_update'] = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            obj['status'] = input('Статус товара продано/продается: ')
            break
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=4)



def get_price():
    price_ = int(input('Введите цену: '))
    data = get_all_data()
    for obj in data:
        if obj['price'] > price_:
            print(obj)


def buy():
    id = input('Введите id товара')
    data = get_all_data()
    for key in data:
        if key['id'] == id:
            summa = int(input('Введиите сумму '))
            if key['price'] <= summa:
                key['status'] = 'Продано'
            with open(FILE, 'w') as f:
                json.dump(data, f, indent=4)
            return None
        for list in data:
            print('Такого id не существует!', '\n')
            print('id', list['id'], list['title'], list['price'])
# buy()

def interface():
    text = (
        """
        0. Список функций
        1. create - создать новый продукт
        2. delete - удалить продукт по id
        3. list - получить список всех продуктов
        4. retrieve - получить продукт по id
        5. update - изменить данные
        6. filte price - фильтрация по цене
        7. exit - выйти из программы
        """  
    )
    print(text)
    while True:
        name = input()
        if name == '0':
            print(text)
        elif name == '1':
            create_data()
        elif name == '2':
            delete_data()
        elif name == '3':
            print(get_all_data())
        elif name == '4':
            get_data_by_id()
        elif name == '5':
            update()
        elif name == '6':
            get_price()
        elif name == '7':
            break
        else:
            print('Функция с таким номером отсутствует')
            break
interface()
