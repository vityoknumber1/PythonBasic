#Математичні класи

class1 = int(input("Enter amount of pupils in the 1st class: "))
class2 = int(input("Enter amount of pupils in the 2nd class: "))
class3 = int(input("Enter amount of pupils in the 3rd class: "))

sum_classes = class1 + class2 + class3
desks_amount = sum_classes // 2

if class1 %2 == 0 and class2 %2 == 0 and class3 %2 == 0:
    print("Desks amount: ", desks_amount)
elif class1 %2 == 1 and class2 %2 == 1 and class3 %2 == 1:
    print("Desks amount: ", desks_amount + 2)
else:
    print("Desks amount: ", desks_amount + 1)