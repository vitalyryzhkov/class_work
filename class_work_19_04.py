
while True:
    print("Привет, Богатырь!")
    print("1: > смерть найдешь")
    print("2: < полцарства найдешь")
    print("3: коня потеряешь")
    choice = input("Твой выбор: ('q' - for exit)")

    if choice == 'q':
        break

    if choice == 1:
        print("Сам")

    elif choice == 2:
        print("Bingo!")

    elif choice == 3:
        print("Horse  ")

    # if choice < 1 or choice > 3:
    else:
        print("Учи матчасть!")


# x = 100

# while x <= 3000:
#     if x%4 == 0 and x%100 != 0 or x%400==0:
#          print("x=", x)
#     x = x + 1

# summa = 0
# while x <= 1000:
#     print("x=", x)
#     summa = summa + x
#     x = x + 1
# print(summa)

# while x <= 100:
#     if x%2 == 0:
#         summa = summa + x
#     x = x + 1
# print(summa)

# while x <= 200:
#     summa = summa + x**2
#     print(summa)
#     x = x + 1

# x = 0
# while x <= 100:
#     print("x=", x)
#     if x%2 == 0:
#         break
#     x = x + 1

# for x in range(200, 100, -2):
#     print(x)

# for x in "Monty Python":
#     print(x)
#
# for x in [1, 2, 3]:
#     print(x)

# for x in range(100, 201):
#     if x%2 == 0:
#        print(x)

# for c in "Страницы, открытые в этом окне, не останутся в истории браузера или поиска. Они не оставят на компьютере следов, таких как файлы cookie, после того как вы закроете все вкладки инкогнито. Скачанные вами файлы и добавленные закладки будут сохранены.":
#     if c.isupper():
#         print(c)
# summa = 0
# summa1 = 0
# summa2 = 0
# s = "Страницы, открытые в этом окне, не останутся в истории браузера или поиска. Они не оставят на компьютере следов, таких как файлы cookie, после того как вы закроете все вкладки инкогнито. Скачанные вами файлы и добавленные закладки будут сохранены."
# for c in s:
#     if c.islower():
#         print(c)
#         summa = summa + 1
#     if c.isupper():
#         # print(c)
#         summa1 = summa1 + 1
#     if c.isupper():
#         # print(c)
#         summa1 = summa1 + 1
#     if c.isspace():
#         summa2 = summa2 + 1
# print(summa)
# print(summa1)
# print(summa2)
