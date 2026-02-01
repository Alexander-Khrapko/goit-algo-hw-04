import os

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args:list,contacts:dict)->str:
    name = args[0]
    phone = args[1]

    if name in contacts:
        contacts[name] = phone
        return f'The contact: {name} already exists. Contact added.'
    else:
        contacts[name] = phone
        return f'Contact added.'

def change_contact(args:list,contacts:dict)->str:
    name = args[0]
    phone = args[1]

    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} changed"
    else:
        return f"Contact {name} not found"

def show_phone(args:list,contacts:dict)->str:
    name = args[0]

    if name in contacts:
        return f"Contact {name} - {contacts[name]}"
    else:
        return f"Contact {name} not found"

def show_all(contacts:dict)->str:
    if len(contacts) == 0:
        return 'No contacts in the list.'

    lines = []  # создаём пустой список для строк контактов

    for name, phone in contacts.items():  # проходим по каждому элементу словаря
        contact_str = name + " — " + phone  # формируем строку для одного контакта
        lines.append(contact_str)  # добавляем эту строку в список

    result = "\n".join(lines)  # объединяем все строки через перенос строки
    return result


def main():
    contacts = {}
    os.system('cls')
    print("Welcome to the assistant bot!")
    while True:
        command, *args = parse_input(input('Enter command: '))

        if not command:
            print('Invalid command!')
            continue
        elif command in ['close', 'exit']:
            print ('Good bay!')
            break
        elif command == 'hello':
            print ('How can I help you?')
        elif command == 'add':
            if len(args) != 2:
                print('The "add" command requires a name and phone number.')
            else:
                print(add_contact(args,contacts))
        elif command == 'change':
            if len(args) != 2:
                print('The "change" command requires a name and new phone number.')
            else:
                print(change_contact(args,contacts))
        elif command == 'phone':
            if len(args) != 1:
                print('The "phone" command requires a name.')
            else:
                print(show_phone(args,contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command!')


if __name__ == '__main__':
    main()
