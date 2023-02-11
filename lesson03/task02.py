#Квадрати натуральних чисел
while True:
    num = int(input("Enter integer number: "))
    print(num, end= "   ")

    counter = 1
    while counter ** 2 <= num:
        print(counter ** 2, end= " ")
        counter += 1

    print("\n")

    if num == 0:
        break
