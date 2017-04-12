# a = 10
# b = 2
#
# is_zero = b==0
#
# def is_zero(x):
#     return x==0
#
# if is_zero(b):
#     print("Zero division error!")
#
# else:
#     result = a/b
#     print("Res of a/b:", result)
#
# if b!=0: тоже самое, что и if not is_zero:
#     result = a / b
#     print("Res of a/b:", result)
# else:
#     print("Zero division error!")

def is_zero(x):
    return x==0

# def is_leap_year(year):
#     reminder = year%4
#     if reminder==0:
#         return True
#     else:
#         return False
#
# print(is_leap_year(2017))

# def is_millennium(year):
#     result = year%1000
#     return result == 0
#
# def is_millennium(year):
#     return not year%1000
#
# print(is_millennium(2000))

# word = "word"
# c = word[0]
#
# if c=='a' or 'A':
#     print("Word starts with 'a'")
# else:
#     print("Word doesn't start with 'a'")

# x = 5
# y = 199
# z = 5
# if x>=3 and x<=7 and y >= z or z == 5:
#     print("Inside")
# else:
#     print("Outside")

print("Привет, Богатырь!")
print("1: > смерть найдешь")
print("2: < полцарства найдешь")
print("3: коня потеряешь")
choice = int(input("Твой выбор: "))

if choice == 1:
    print("Сам")

elif choice == 2:
    print("Bingo!")

elif choice == 3:
    print("Horse  ")

# if choice < 1 or choice > 3:
else:
    print("Учи матчасть!")
