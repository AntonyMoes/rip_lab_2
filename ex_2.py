#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['ABc', 'aBC', 'qwe', 'QWE']

# Реализация задания 2

if __name__ == '__main__':
    print(' '.join([str(v) for v in Unique(data1)]))
    print(' '.join([str(v) for v in Unique(data2)]))
    print(' '.join([str(v) for v in Unique(data3)]))
    print(' '.join([str(v) for v in Unique(data3, ignore_case=True)]))
