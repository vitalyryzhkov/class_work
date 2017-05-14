# comprehension
# почитать про lambda функцию

# lst = [-5, 3, 4]
# max_elem = max(lst)
# min_elem = min(lst)
# if max_elem < min_elem:
#     abs_max = max_elem
# else:
#     abs_max = min_elem
# for i in range(len(lst)):
#     lst.append((lst[i] / abs_max))
#
# print(lst)

dict_planets = {'earth': 345778, 'mars': 47789, 'venus': 4679339}
cars = {'MB': ['A', 'B', 'G', 'S', 'GLs'], 'BMW': ['3-s', '5-s', '7-s']}
cars['AUDI'] = ['A4', 'A6', 'A*8']
cars['AUDI'].append('A5')
# if 'MB' in cars:
#     tm_cars = cars['MB']
# if 'AUDI' in cars:
#     print(cars)
#     del cars['AUDI']
# print(cars)

# for key in cars:
#     print (key)
#
# for key in cars:
#     print (key, "->", cars[key])
#
# for key, value in cars.items():
#     print ("%s -> %s" % (key, value))

# def get_value_by_key(key):
#     return dict_planets[key]
#
# for key in sorted(dict_planets, key = get_value_by_key):
#     print (key, "->",  dict_planets[key])
#
# for key in sorted(dict_planets, key = dict_planets.get):
#     print (key, "->",  dict_planets[key])
#
# for key in sorted(dict_planets):
#     print(key, "->", dict_planets[key])

        # for key in sorted(cars, key=cars.get):# reverse=True):
#     print (key, "->",  cars[key])

# dict_vocab_en_es = {'world': 'mundo', 'language': 'idioma', 'See you later': 'Hasta la vista'}
# print(dict_vocab_en_es)

# def get_value_by_key(key):
#     return dict_planets[key]

# for key in sorted(dict_vocab_en_es, key = dict_vocab_en_es.get):
#     print (key, "->",  dict_vocab_en_es[key])

# dict_planets_2 = {'earth': (345778, 894202), 'mars': (47789, 898902), 'venus': (4679339, 238000)}
# print(dict_planets_2)
#
# def get_value_by_key(key):
#     return dict_planets_2[key][1]
#
# for key in sorted(dict_planets_2, key = get_value_by_key):
#     print(key, "->",  dict_planets_2[key])
"""
employee_1 = {"name":"Alex", "salary": 10000, "dep": "Sales", "bonus":200}
employee_2 = {"name":"Nick", "salary": 20000, "dep": "Sales"}
employee_3 = {"name":"Sue",  "salary": 50000, "dep": "IT", "bonus":500}
employee_4 = {"name":"Phil", "salary": 5000,  "dep": "BoardOfDirectors", "bonus":10000}

employees = [employee_1, employee_2, employee_3, employee_4]

def foo(dict):
    return dict['salary']
    # return dict.get('salary')

# employees.sort(key=foo, reverse = True) - меняем полностью списко словарей
# employees.sort(key=lambda dict: dict.get('salary'), reverse = True)
for elem in sorted(employees, key=foo, reverse = True):
    print(elem['name'], elem['salary'])
print(employees)
"""
# f = open("D:\\test.txt", mode="w")
# f.write("abc")
# f.close()
# f = open("D:\\test.txt")
# print(f.read())
# f.close()
#
# f = open("D:\\test.txt", mode="a")
# f.write("bsa")
# f.close()
# f = open("D:\\test.txt")
# print(f.read())
# f.close()
"""
d = {}

f = open("D:\\war_peace.txt")
s = f.read().lower()

# print(s[:100])

for c in s:
    if ord(c) in range(ord('а'), ord('я')+1):
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

print(d)

# def get_value_by_key(key):
#     return d[key]
for key in sorted(d, key = d.get, reverse = True):
# for key in sorted(d):
    normilized_lenghth = int(d[key]/5000)
    print("%s - > \t%s:\t%s" % (key, d[key], normilized_lenghth*"="))

f.close()
"""
