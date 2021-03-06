'''
Задание # 6*
Реализовать структуру данных « Товары ». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами (характеристиками товара: название,
цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например название, а значение — список значений-характеристик,
например список названий товаров.
Пример:
{
'название': ['компьютер', 'принтер', 'сканер'],
'цена': [20000, 6000, 2000],
'количество': [5, 2, 7],
'ед': ['шт.']
}
'''

'''
Само решение занимет 8 строк
 + несколько строк для определения остновного списка. 
 
 Я добавил в него еще одну характеристику которая есть не у всех товаров. Чтобы было интереснее. 
 Без этого условия решение вообще в 4 строчки можно было бы записать. Наверное

Собственно решение без ввода и вывода выглядит так:

1) Получения списка всех характеристик с помощью функции reduce,
2) С помощью 2-х вложенных функций map( ... , map(...)) получаем новый словарь. Но т.к. я добавил новую характеристику
    то нужно удалять значения None. А у множеств этот без цикла не получается. Почему-то

from functools import reduce 
goods_list = [[]] + goods_list
char_name_list = list(set(reduce(lambda x, y: x + list(y[1].keys()), goods_list))) 
goods_list.pop(0)
result_dict = {}
for el in char_name_list:
    an_set = set(map(lambda x: x[1].get(el), goods_list))
    an_set.discard(None)
    result_dict.setdefault(el, list(an_set))

'''
# Для первого способа понадосится прикольная функция reduce, а для этого нужно подключить модуль functools
from functools import reduce

goods_list = [
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.', 'Акция': 'Скидка 17%'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'}),
(4, {'название': 'жидкость для протирки мониторов', 'цена': 150, 'количество': 0.7, 'eд': 'л.'}),
(5, {'название': 'ручка брэндированная', 'цена': 20, 'количество': 1500, 'eд': 'шт.', 'Акция': 'Подарок'})
]

# Для применения функции reduce() необходимо создать технический пустой список вначале
goods_list = [[]] + goods_list

char_name_list = list(set(reduce(lambda x, y: x + list(y[1].keys()), goods_list)))
char_name_list.sort()
print(f'Список всевозможных характеристик: {char_name_list}')

# Удаление технического пустого списка вначале
goods_list.pop(0)
result_dict = {}

for el in char_name_list:
    an_set = set(map(lambda x: x[1].get(el), goods_list))
    an_set.discard(None)
    result_dict.setdefault(el, list(an_set))

print('')
print(f'Результат работы алгоритма: {result_dict}')
print('')
print('Результат работы алгоритма оформленный почти как в задании:')
print('{')
list(map(lambda x: print(f'{x},'), result_dict.items()))
print('}')
