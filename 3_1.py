def num_translate(numb):
    """
    функция переводчик
    :param numb: введите прописные цифры от 0 до 10
    :return:возвращает слово на русском
    """

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
    return num_slov.get(numb.lower())


some_num_en = 'One'
print(num_translate(some_num_en))
