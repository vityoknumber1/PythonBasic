#Перевернути число

num = int(input("Enter the number: "))

sot = num // 100
des = (num - sot * 100) // 10
od = (num - sot * 100) - des * 10

print("Reverse number: ", od, des, sot)