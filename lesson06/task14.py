#Унікальні числа в списках

list1 = [1, 2, 2, 4 , 7, 9]
list2 = [1, 2, 3, 10, 7]
print("List1", list1)
print("List2", list2)

print("Unique elements", (set(list1) ^ set(list2)), "\nCount of unique elements:", len((set(list1) ^ set(list2))))