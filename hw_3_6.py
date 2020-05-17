'''
Задание # 6

Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
использовать написанную ранее функцию int_func().
'''

def int_func(str_var):
    return str_var.capitalize()


str_var = input('Введите строку со словами разделенными проблелом. Желательно только прописными буквами: ').lower()
str_list = str_var.split()
str_list = map(int_func, str_list)
str_var = ' '.join(str_list)
print(f'Текущий результат суммирования всех введенных чисел: {str_var}')