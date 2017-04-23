# while True:
#     print("Привет, Богатырь!")
#     print("1: > смерть найдешь")
#     print("2: < полцарства найдешь")
#     print("3: коня потеряешь")
#     choice = input("Твой выбор: ('q' - for exit)")
#
#     if choice == 'q':
#         break
#
#     if int(choice) < 1 or int(choice) > 3:
#         print("Учи матчасть!")
#         continue
#
#     if int(choice) == 1:
#         print("Сам")
#
#     elif int(choice) == 2:
#         print("Bingo!")
#
#     elif int(choice) == 3:
#         print("Horse  ")
#
#     # if choice < 1 or choice > 3:
#     # else:
#     #     print("Учи матчасть!")

import random

def fill_truck(weight_limit):
    total_boxes = 0
    total_weight = 0
    while (total_weight < weight_limit):
        box_weight = random.randint(1, 100)
        free_space = weight_limit - total_weight
        if free_space < box_weight:
            print(box_weight)
            continue

        total_weight = total_weight + box_weight
        total_boxes = total_boxes + 1
        print("Total weight = %d, num. of boxes = %d" %
              (total_weight, total_boxes))
# fill_truck(2000)

def fill_truck_fixed(weight_limit, box_weight):
    total_weight = 0
    num_boxes = weight_limit // box_weight
    for x in range(1, num_boxes + 1):
        total_weight = total_weight + box_weight

        print(total_weight, x)
# fill_truck_fixed(2000, 50)

# def random_numbers(num_randoms):
#     for i in range(num_randoms):
#         x = random.randint(0, 100)
#
#         print(x)
# random_numbers(100)

# def max_random_numbers(num_randoms):
#     max_num = 0
#     for i in range(num_randoms):
#         num = random.randint(0, 100)
#         print(num)
#         if(num > max_num):
#             max_num = num
#
#     return max_num
#
# max_num = max_random_numbers(10)
# print("Max number = ", max_num)

# def min_random_numbers(num_randoms, lower_limit, upper_limit):
#     min_num = upper_limit
#     for i in range(num_randoms):
#         num = random.randint(lower_limit, upper_limit)
#         print(num)
#         if(num < min_num):
#             min_num = num
#     return min_num
# min_num = min_random_numbers(10, 0, 100)
# print("Min number = ", min_num)

# def avr_random_numbers(num_randoms, lower_limit, upper_limit):
#     avr_num = 0
#     for i in range(num_randoms):
#         num = random.randint(lower_limit, upper_limit)
#         print(num)
#         avr_num = avr_num + num
#     print("----------", avr_num)
#
# avr_random_numbers(10, 0, 10)

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_num = fib(10)
print(fib_num)
