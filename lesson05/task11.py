#Видалення елемента зі списку

import random

list_num = []

for a in range(10):
    list_num.append(random.randint(0, 100))

print("Initial list of numbers: ", list_num)

k = int(input("Print index k of element: "))

for i in range(k+1, len(list_num)):
    list_num.insert(k, list_num.pop())

list_num.pop()

print("Final: ", list_num)