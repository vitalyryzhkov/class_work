
# lst = [1, 2, 3, 4, 5]
# b = lst[-1]
# lst[-1] = lst[0]
# lst[0] = b

# print(lst)

# for c in lst:
#     print(c**2)

# for i, elem in enumerate(lst):
#     print(i, elem)
#     lst[i] = elem**2
#
# print(lst)

# lst = [1, 2, 3, 4, 5]
# for i, elem in enumerate(lst):
#     lst[i] = elem**3

# for i in range(len(lst)):
# for i in range(0, len(lst), 3):
#     print(lst[i])
#     lst[i] = lst[i]**3
# print(lst)

def create_random_list(num, lower_limit, upper_limit):
    import random
    lst = []
    for i in range(num):
        lst.append(random.randint(lower_limit, upper_limit))
    return lst

def print_list(lst):
    for elem in lst:
        print("Element of the list is equal to", elem)

def print_list_2(lst):
    for i, elem in enumerate(lst):
        print("%dth element of the list is equal to %d" % (i, elem))

def print_list_3(lst):
    for i in range(len(lst)):
        print("%dth element of the list is equal to %d" % (i, lst[i]))

def max_list_elem(lst):
    max_elem = lst[0]
    for elem in lst:
        # max
        if elem > max_elem:
            max_elem = elem
    return max_elem

def square_list(lst):
    for i, elem in enumerate(lst):
        lst[i] = elem ** 2

def square_list_2(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2

def sum_list_elem(lst):
    sum_elem = 0
    for elem in lst:
        sum_elem += elem
    return sum_elem

def min_list_elem(lst):
    min_elem = lst[0]
    for elem in lst:
        if elem < min_elem:
            min_elem = elem
    return min_elem


def normalize_name_of_planets(planets):
    for i, planets in enumerate(planets):
        planets.remove(planets[0])

    print(planets)

normalize_name_of_planets([' mercury', ' mars', ' earth', ' venus'])

lst = create_random_list(10, 0, 100)
# print_list_2(lst)
min_list_elem(lst)
# print("Max:", max_list_elem(lst))
# print("Min:", min_list_elem(lst))

# sum
# min
# normalize list of planets: planets = [' mercury', ' mars', ' earth', ' venus']
