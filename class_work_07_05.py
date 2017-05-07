# lst = ['aaaa', 'ccc', 'bb', 'd']
# # lst.sort()
# lst.sort(key=len)
# print(lst)
#
# lst = ['aaaaz', 'ccca', 'bb', 'd']
# def reversed_sort(elem):
#     return elem[::-1]
# lst.sort(key=reversed_sort)
# print(lst)

# lst = [-1, 10, 15, -12, 5, -6]
# lst.sort(key=abs)
# print(lst)

# dist = [2, 4, 7, 8, 4, 11, 10, 12]
# my_position = 9
#
# def diff_dist(elem):
#     return abs(elem - my_position)
# dist.sort(key=diff_dist)
# print(dist)

# last_name = ['Александр Малышев', 'Александр Скворцов', 'Алексей Кулишенко', 'Андрей Кравчук',
#              'Андрей Рожко', 'Виктор Бурлаков', 'Виктор Горовой', 'Виталий Рыжков', 'Виталина Гавеля',
#              'Владимир Веренчук', 'Екатерина Шадрина', 'Надежда Симанович', 'Николай Марушевский']
# def sort_by_surname(elem):
#     return elem.split()[1] + " " + elem.split()[0]
#
# last_name.sort(key=sort_by_surname)
# print(last_name)

# import random
#
# table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# def print_table(table):
#     for line in table:
#         for elem in line:
#             print(elem, end=" ")
#         print()
#
# def fill_random_table(table):
#     for idx1, line in enumerate(table):
#         for idx2, elem in enumerate(line):
#             table[idx1][idx2] = random.randint(1, 50)
#
# print_table(table)
# fill_random_table(table)
# print_table(table)

# table = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
#
# def print_table(table):
#     for line in table:
#         for elem in line:
#             print(elem, end="\t")
#         print()
#
# def fill_pifagor_table(table):
#     for idx1, line in enumerate(table):
#         for idx2, elem in enumerate(line):
#             table[idx1][idx2] = ((len(line) - idx1) * ((len(line) - idx2)))
#
# fill_pifagor_table(table)
# print_table(table)

# table = [[0]*10]*10
# table[0][0] = 42
# print(table)

# table = [[0 for i in range(10)] for j in range(10)]
# print(table)
# table[0][0] = 42
# print(table)

# def foo(*args):
#     print(args)
#     for i in args:
#         print(i)
#
# foo(1, 2, 3)

