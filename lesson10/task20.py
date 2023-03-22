#Сортування матриці
import random

while True:
    M = int(input("Enter size of matrix МхМ: "))

    if M <= 5:
        print("Enter integer number more than 5")
    else:
        break

matrix = [[random.randrange(1, 50) for x in range(M)] for y in range(M)]

print("Initial matrix")

for row in matrix:
    for col in row:
        print(f"{col:<4}", end="\t")
    print()

sum_list = []

for row_l in list(map(list, zip(*matrix))):
    sum_l = 0
    for i in row_l:
        sum_l += i
    sum_list.append(sum_l)
print("Sum of columns\n", sum_list)

def bubble_sort(list_to_sort):
    for _ in range(0, len(list_to_sort) - 1):
        for x in range(0, len(list_to_sort) - 1):
            if list_to_sort[x] > list_to_sort[x + 1]:
                list_to_sort[x], list_to_sort[x + 1] = list_to_sort[x+1], list_to_sort[x]
    return list_to_sort

def bubble_sort2(list_to_sort):
    for _ in range(0, len(list_to_sort) - 1):
        for x in range(0, len(list_to_sort) - 1):
            if list_to_sort[x] < list_to_sort[x + 1]:
                list_to_sort[x], list_to_sort[x + 1] = list_to_sort[x+1], list_to_sort[x]
    return list_to_sort

matrix_sorted = [bubble_sort2(list(map(list, zip(*matrix)))[i]) if i % 2 == 0 else bubble_sort(list(map(list, zip(*matrix)))[i]) for i in range(len(matrix))]

print("Matrix after sorting")
for col in range(M):
    for row in matrix_sorted:
        print(f"{row[col]:<4}", end="\t")
    print()

print("\t\t".join([str(a) for a in bubble_sort(sum_list)]))