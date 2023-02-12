# Послідовності цілих чисел

total = 0
counter = 0

maximum = 0
minimum = None

i = 0
j = 0

while True:

    num = int(input("Enter integer number: "))

    if num == 0:
        break
    elif minimum is None:
        minimum = num
    elif num < minimum:
            minimum = num

    if num > maximum:
        maximum = num

    if num %2 == 0:
        i +=1
    else:
        j +=1

    counter += 1
    total += num
    avg = total / counter

print("Amount: ", counter)
print("Sum: ", total)
print("Average: ", avg)
print("Max number: ", maximum)
print("Min number: ", minimum)
print("Even and odd count: ", i, j, sep="\n")





