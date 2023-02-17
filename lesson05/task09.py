#Сусіди
import random

list1 = []

for i in range(10):
    list1.append(random.randint(0, 100))

print("List of numbers: ", list1)

n = 0
for j in range(1, len(list1)-1):
    if list1[j+1] < list1[j] and list1[j] > list1[j-1]:
        n += 1

print("Count of greatest numbers then their neighbours: ", n)