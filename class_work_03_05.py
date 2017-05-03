# lst = [x for x in range(1,101)]
# print(lst)

# lst = [x**2 for x in range(1,101)]
# print(lst)
# lst = [x**2 for x in range(1,101) if x**2 % 5 == 0]
# print(lst)
# lst = [x**3 for x in range(1, 11)]
# print(lst)
# lst = [x for x in [1, 2, 3]]
# print(lst)
# ??????? [str(x) for x in [1, 2, 3]]
# print(sum([x for x in range(100)]))
# print(min([x for x in range(100)]))
# print(max([x for x in range(100)]))

# lst = [x for x in range(1,101) if x % 2 !=0]
# print(lst)
# def max_min_diff(lst):
#     a = max([x for x in lst])
#     b = min([x for x in lst])
#     print(a - b)
#
# max_min_diff(lst)

# Даны 2 списка целых чисел. Вернуть True если они имеют одинаковый первый или одинаковый последний элемент.

# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True
# lst = [1, 2, 3]
# lst2 = [1, 3]
#
# def common_end(lst, lst2):
#     if lst[0] == lst2[0] or lst[-1] == lst2[-1]:
#         return True
# print(common_end(lst, lst2))

# Дан cписок целых чисел. Вернуть список, состоящий из двух элементов: первого и последнего.

# make_end([1, 2, 3]) → [1,3]
# make_end([4, 2]) → [4,2]
# lst = [1, 2, 3]
# print(lst)
# def make_end(lst):
#     lst = [lst[0], lst[-1]]
#     return lst
# print(make_end(lst))

# Дан cписок целых чисел. Вернуть True, если список содержит 2 подряд идущие 2-ки.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

