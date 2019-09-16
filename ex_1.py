#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1

if __name__ == '__main__':
    goods = [
       {'title': 'Ковер', 'price': 2000, 'color': 'green'},
       {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print('\n'.join([str(v) for v in field(goods, 'qwe', 'color')]))
    print('\n'.join([str(v) for v in gen_random(1, 3, 5)]))
