def thesaurus(*names):
    some_dict = {}
    for name in names:
        key = name[0].capitalize()
        if key not in some_dict:
            some_dict[key] = []
        some_dict[key].append(name)
    return some_dict


print(thesaurus("Иван", "Мария", 'Аня', "Петр", "Илья"))
# some_d = thesaurus("Иван", "Мария", 'Аня', "Петр", "Илья")
# print(sorted(some_d))
# сортировка возвращает ключи или значения списком, если нужно записать в словарь надо изначально отсортировать
# и написать функцию принимающий список, либо отдельно код вне функции но при этом придется создавать еще один словарь
