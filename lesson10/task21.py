#Сума позицій матриці
import random

m = int(input("Введіть кількість рядків матриці: "))
n = int(input("Введіть кількість стовпців матриці: "))

print(m, n)

matrix = [[random.randrange(0, 50) for x in range(n)] for y in range(m)]

sum_of_columns = []
def sum_columns(matrix):
    for j in range(n):
        sum_of_column = 0
        for i in range(len(matrix)):
            sum_of_column += matrix[i][j]
        sum_of_columns.append(sum_of_column)
        print(sum_of_column, end="\t")

def sum_rows(matrix):
    for j in range(m):
        sum_of_column = 0
        for i in range(len(matrix)):
            sum_of_column += matrix[i][j]
        sum_of_columns.append(sum_of_column)
        print(sum_of_column, end="\t")

print("Final matrix")
for i in matrix:
    print('\t'.join(map(str, i)))
sum_columns(matrix)
sum_rows(list(map(list, zip(*matrix))))
