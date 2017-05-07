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

group = [
('Александр Скворцов', '1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Андрей Рожко', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0'),
('Алексей Кулишенко', '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Виталий Рыжков', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0'),
('Виталина Гавеля', '1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Виктор Бурлаков', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0'),
('Виктор Горовой', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0'),
('Надежда Симанович', '1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Николай Марушевский', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Андрей Кравчук', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0'),
('Екатерина Шадрина', '1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'),
('Александр Малышев', '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0'),
('Владимир Веренчук', '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
]

def print_full_names(group):
    for student in group:
        name = student[0]
        rank = student[1]
        print()
# print_full_names(group)

def print_full_reverse_names(group):
    for student in group:
            full_name = student[0]
            lst_full_name = full_name.split()
            fist_name = lst_full_name[0]
            second_name = lst_full_name[1]
            print(second_name, fist_name)
# print_full_reverse_names(group)

def print_full_names_sorted(group):
    def sort_by_surname(elem):
        return elem.split()[1] + " " + elem.split()[0]
    lst_student = []
    for student in group:
        lst_student.append(student[0])
    lst_student.sort(key=sort_by_surname)
    print(lst_student)

# print_full_names_sorted(group)

def print_ranks(group):
    for rank in group:
            all_rank = rank[1]
            lst_all_rank = all_rank.split(",")
            rank_total = lst_all_rank.count('1')

            print(rank[0], rank_total)

# print_ranks(group)

def get_ranks_sorted(group):
    def sort_by_surname(elem):
        return elem.split()[2] + " " + elem.split()[0]
    lst_name_and_rank_total = []
    for elem in group:
        name = elem[0]
        all_rank = elem[1]
        lst_all_rank = all_rank.split(",")
        rank_total = lst_all_rank.count('1')
        name_and_rank_total = name + " " + str(rank_total)

        lst_name_and_rank_total.append(name_and_rank_total)
        lst_name_and_rank_total.sort(key=sort_by_surname)
        # lst_name_and_rank_total

        print(name_and_rank_total)

get_ranks_sorted(group)

def print_top_n(students_rank, n):
    pass
