# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

from os import path

file_base = "base.txt" # имя базы для экспорта и импорта
all_data = [] # пустой список
last_id = 0 # порядковый номер записи

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, last_id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
        return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty base!\n")

def add():
    with open(file_base, "a", encoding="utf-8") as base:
        base.write(input('Введите ФИО: ') + ' ')
        base.write(input('Введите номер тел: ') + '\n')
    print(base)

def search():
    with open(file_base, "r", encoding="utf-8") as base:
        a = input('Введите любое значение ФИО: ')
        book = base.read().split('\n')
        for i in book:
            if a in i:
                print(i)

def change():
    people = search()
    with open(file_base, "w+", encoding="utf-8") as base:
        old_name = input('Изменить имя: ')
        new_name = input('Новое имя: ')
        people = old_name
        for i in base:
            if old_name == i:
                base.read.ln(old_name), old_name.write(new_name + '\n')

def delete():
    with open(file_base, "w+", encoding="utf-8") as base:
        name = input('Кого удаляем: ')
        book = base.read().split('\n')
        for i in book:
            if name in i:
                print(i)
                for i in base:
                    if i == base:
                        base.write(i)


def main_menu():
    work = True
    while work:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all\n"
                       "2. Add\n"
                       "3. Search\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add()
            case "3":
                search()
            case "4":
                change()
            case "5":
                pass
            case "6":
                pass
            case "7":
                work = False
            case _:
                print("Try again!\n")

main_menu()