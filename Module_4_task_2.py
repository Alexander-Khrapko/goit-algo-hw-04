import os

# ФАЙЛ cats.txt
# 60b90c1c13067a15887e1ae1,Tayson,3,5          ошибка данных 4
# 60b90c2413067a15887e1ae2,Vika,1
# 60b90c2e13067a15887e1ae3,Barsik,2
# 60b90c3b13067a15887e1ae4,Simon,12
# 60b90c4613067a15887e1ae5,Tessi,5
# 60b90c2413067a15887e1ae2,Grey,3              ошибка id совпадает с Vika

# Файл содержит данные о котах, где каждая запись содержит уникальный идентификатор, имя кота и его возраст.
# Функция должна возвращать список словарей, где каждый словарь содержит информацию об одном коте.

def get_cats_info(path) -> list[dict]:
    new_list_cats = []
    id_cat = set()
    if not path:        # проверка на пустую строку в переменной 'path'
        print('Ви не вказали файл з даними.')
        return []

    try:
        with (open(path, 'r', encoding='utf-8') as fh):

            for line in fh:                 # проходим построчно по всему файлу
                line = line.strip()
                if not line:                # проверяет конец файла пустую строку
                    continue
                list_cats = line.split(',')

                if len(list_cats) != 3:     # проверяет кол-во данных в строке их должно быть 3
                    print (f'Строку {line} пропускаємо, неправильні дані')
                    continue

                id, name, age = list_cats

                if id in id_cat:            # проверяет уникальность id
                    print (f"Два id {id} однакові, кота на им'я {name} пропускаємо")
                    continue
                id_cat.add(id)


                new_list_cats.append({
                  'id': id,
                  'name': name,
                  'age': age
                })

            return new_list_cats

    except FileNotFoundError:               # ошибка в названии файла, пути или его нет
        print(f"Ошибка: файл '{path}' не найден.")
        return []

os.system('cls')
print (get_cats_info("cats.txt"))

