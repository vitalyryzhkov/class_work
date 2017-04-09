# def print_delim():
#     print("----------------------------------")
#
# def print_delim1(num_repeats = 40):
#     print("*" * 40)
#
# print_delim1()
#
# def pretty_print(value):
#     print("---------")
#     print("Value =", value)
#     print("---------")
#
# def pretty_print1(value, description = "Value ="):
#     print("---------")
#     print(description, value)
#     print("---------")
#
#
# def square_rect(width, height):
#     return width*height
#
# def square_square(width):
#     result = square_rect(width, width)
#     return result
#
# def add_and_multiply(a, b = 42):
#     sum = a+b
#     mult = a*b
#     return sum, mult
#
# result1, result2 = add_and_multiply(2, 3)
# print(result1)
# pretty_print(result2)
#
# def empty_func():
#     pass
#
# square = square_rect(12, 10)
# print_delim()
# print(square)
# print_delim()
#
# square2 = square_square(4)
# pretty_print(square2)
#
# print_delim()

# def cel2far(c):
#     result = 9/5 * c + 32
#     return result
#
# print(cel2far(15))
#
# def far2cel(f):
#     result = 5/9 * (f - 32)
#     return result
#
# print(far2cel(15))
#
# def c2f_f2c(cel, far):
#     cels = 9/5 * cel + 32
#     faren = 5/9 * (far - 32)
#     return cels, faren
#
# print(c2f_f2c(15, 451))

# import math
#
# def cirkle(r):
#     return math.pi * r**2
#
# print(cirkle(5))

a = 123

def summ(a = input("Enter: ")):

    return summ(a)

print(summ(a))
