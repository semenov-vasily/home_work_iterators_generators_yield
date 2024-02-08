import types


# Класс итератора
class FlatIterator:

    def __init__(self, list_of_list):
        # Определяет атрибут для хранения списка списков
        self.list_of_list = list_of_list

    def __iter__(self):
        # Индекс списка внутри общего списка
        self.list_num = 0
        # Индекс элемента списка
        self.num_in_list = -1
        return self

    def __next__(self):
        # Индекс элемента списка увеличиваем на 1, первый индекс будет 0
        self.num_in_list += 1
        # Проверяем, что индекс элемента списка не сравнялся с длинной списка
        if self.num_in_list == len(self.list_of_list[self.list_num]):
            # Если сравнялся - переходим к следующему списку внутри общего списка
            self.list_num += 1
            # Сбрасываем индекс элемента списка до 0
            self.num_in_list = 0
            # Если номер списка сравнялся с длинной общего списка останавливаем итерацию
            if self.list_num == len(self.list_of_list):
                raise StopIteration
        # Присваиваем переменной item значение элемента списка по
        # индексу списка и индексу элемента списка и возвращаем ее
        item = self.list_of_list[self.list_num][self.num_in_list]
        return item


# Функция, сравнивающая результат, возвращенный FlatIterator с эталонным
def test_1(lists):
    # Исходный список списков
    list_of_lists_1 = lists

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# Функция генератора
def flat_generator(list_of_lists):
    # Проходимся по спискам
    for list_in_list in list_of_lists:
        # Проходимся по значениям в каждом списке
        for data_in_list in list_in_list:
            # Возвращаем значение элемента списка
            yield data_in_list


# Функция, сравнивающая результат, возвращенный flat_generator с эталонным
def test_2(lists):
    # Исходный список списков
    list_of_lists_1 = lists

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':

    # Исходный список списков
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    # Вызываем итератор FlatIterator
    print(f'Вызываем итератор ********************************')
    for item in FlatIterator(list_of_lists_1):
        print(item)

    # Списочное выражение по итератору
    print()
    flat_list_iter = [item for item in FlatIterator(list_of_lists_1)]
    print('list comprehension  по итератору *****************')
    print(flat_list_iter)

    # Вызываем проверочную функцию по итераторам
    test_1(list_of_lists_1)
    print()

    # Вызываем генератор flat_generator
    print(f'Вызываем генератор ********************************')
    for item in flat_generator(list_of_lists_1):
        print(item)

    # Списочное выражение по генератору
    print()
    flat_list_gen = [x for x in flat_generator(list_of_lists_1)]
    print('list comprehension  по генератору *****************')
    print(flat_list_gen)

    # Вызываем проверочную функцию по итераторам
    test_2(list_of_lists_1)
