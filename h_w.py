import random
def print_table(table):
    for line in table:
        for elem in line:
            print(elem, end="\t")
        print()

table = [[0 for i in range(10)] for j in range(10)]

table1 = []

for i in range(len(table)):
    for j in range(len(table[i])):
        table[i][j] = random.randint(1, 101)
print_table(table)
print()

for i in range(len(table)):
    for j in range(len(table[i])):

        if i % 2 == 0:
            table[j].sort()
        else:
            table[i].sort(reverse=True)
print_table(table)

