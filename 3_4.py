def thesaurus_adv(*names):
    surname_dict = {}
    for surname in names:
        key = surname.split()[-1][0]
        if key not in surname_dict:
            surname_dict[key] = {}
        key2 = surname[0]
        if key2 not in surname_dict[key]:
            surname_dict[key][key2] = []
        surname_dict[key][key2].append(surname)
    return surname_dict

name = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(name)  # простой вывод без сортировки
name2 = sorted(name)
sor_dict = {}
for n in name2:
    sor_dict[n] = name[n]

print(sor_dict) # сортировка по ключу фамилий , можно еще добавить сортировку внутреннего словаря при большом желании