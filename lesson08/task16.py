#Трикутники

symbol = int(input("Enter height of the figure in the symbols :"))

#фігура A
print("A figure")
for i in range(1, symbol + 1):
    for j in range (symbol - i):
        print(" ", end = "")

    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end = "")
        else:
            if i == symbol:
                print("*", end = "")
            else:
                print(" ", end = "")
    print()

#фігура B
print("\nB figure")
for i in range(1, symbol + 1):
    for j in range (symbol - i):
        print(" ", end = "")
    for k in range(2 * i - 1):
        print("*", end = "")
    print()

#фігура C
print("\nC figure")
for i in range(symbol):
    for j in range(symbol - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
for i in range(symbol - 1):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(2*(symbol - i - 1) - 1):
        if j == 0 or j == 2*(symbol - i - 1) - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#фігура D
print("\nD figure")
for i in range(symbol):
    for j in range(symbol - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
for i in range(symbol - 1):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(2*(symbol - i - 1) - 1):
        if j == 0 or j == 2*(symbol - i - 1) - 2 or j == symbol - i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()