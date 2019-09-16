from random import randint
from typing import List, Dict


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items: List[Dict], *args):
    assert len(args) > 0
    for item in items:
        d = {}
        for arg in args:
            value = item.get(arg)
            if value is not None:
                d[arg] = value
        if len(d) >= 1 and len(args) > 1:
            yield d
        elif len(d) == 1 and len(args) == 1:
            yield list(d.values())[0]


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin: int, end: int, num_count: int):
    for _ in range(num_count):
        yield randint(begin, end)
