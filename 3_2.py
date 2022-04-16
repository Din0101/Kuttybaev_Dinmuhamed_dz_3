def num_translate(numb):
    num_slov = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'}
    if num_slov.get(numb.lower()) == None:
        return
    if numb[0].istitle() == True:
        return num_slov.get(numb.lower()).title()
    else:
        return num_slov.get(numb.lower())


some_num_en = 'two'
print(num_translate(some_num_en))
