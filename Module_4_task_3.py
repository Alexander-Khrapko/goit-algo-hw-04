import sys
from pathlib import Path
from colorama import Fore, Style, init

# инициализация colorama цвет сбрасывается автоматически после каждого print()
init(autoreset=True)

# рекурсивная функция - раскладывает путь переданный через командную строку
# в виде дерева, где папки ветки, а файлы листья. Папки выделяются синим
# цветом, а файлы зеленым
def print_directory_tree(path: Path, indent: str = "  ") -> None:

    try:
        # сортируем элементы папки сначала папки потом файлы
        # по алфавиту, без учёта регистра и создаем кортеж
        items = sorted(path.iterdir(),key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:     # PermissionError — нет доступа к папке
        print(f"{indent}{Fore.RED}[нет прав доступа]")
        return
    except FileNotFoundError:   # FileNotFoundError — папка исчезла во время выполнения скрипта
        print(f"{indent}{Fore.RED}[данные удалены]")
        return
    except OSError as e:             # OSError — битая ссылка, сетевой диск и т.п.
        print(f"{indent}{Fore.RED}[ошибка: {e}]")
        return

    count = len(items)              # количество элементов в папке
    # проходим по кортежу и нумеруем каждый элемент
    for index, item in enumerate(items, start=1):
        if index == count:
            connector = "└─ "      # если элемент последний
        else:
            connector = "├─ "      # если элемент не последний

        if item.is_dir():
            print(f"{indent}{connector}{Fore.BLUE}{item.name}\\")
            # новый префикс для вложенных элементов
            if index == count:
                extension = "   "   # ветка закончилась, вертикальная линия не нужна
            else:
                extension = "│  "   # ветка продолжается вниз
            print_directory_tree(item, indent + extension)
        else:
            print(f"{indent}{connector}{Fore.GREEN}{item.name}")

    # та же функция но без визуализации  дерева
    # for item in items:
    #     if(item.is_dir()):  # если папка печать голубым и рекурсия
    #         print(f"{indent}{Fore.BLUE}{item.name}\\")
    #         print_directory_tree(item, indent + "  ")
    #     else:               # если файл печать зеленым
    #         print(f"{indent}{Fore.GREEN}{item.name}")

def main():

    # проверяем количество передаваемых аргументов в командной строке
    # python module_4_task_3 - их один имя скрипта
    # python module_4_task_3 c:/install - их два: имя скрипта и путь
    # python module_4_task_3 c:/install pr - их три: имя скрипта, путь и какой-то ключ
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Ошибка: укажите путь к директории")
        sys.exit(1)

    # преобразование строчного аргумента в путь
    path = Path(sys.argv[1])

    # проверка существования введенного как аргумент пути
    # на существование такого пути или это файл
    if not path.exists():       # проверка - существует указанный путь
        print(f"{Fore.RED}Ошибка: путь не существует")
        sys.exit(1)
    elif not path.is_dir():     # проверка - указан файл
        print(f"{Fore.RED}Ошибка: указанный путь не является директорией")
        sys.exit(1)

    print(f"{Fore.BLUE}Корневая директория\n{path.resolve()}\\")
    print_directory_tree(path)

if __name__ == "__main__":
    main()
