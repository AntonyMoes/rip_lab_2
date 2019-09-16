from typing import List, Generator, Union

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items: Union[List, Generator], ignore_case: bool = False):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self._it = iter(items)
        self._ignore_case = ignore_case
        self._used = set()

    def __next__(self):
        while True:
            value = next(self._it)

            if isinstance(value, str) and self._ignore_case:
                m_value = value.lower()
            else:
                m_value = value

            if m_value not in self._used:
                self._used.add(m_value)
                return value

    def __iter__(self):
        return self
