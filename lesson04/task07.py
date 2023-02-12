#Визначення кількості слів у рядку

string = input("Enter string: ")
print(string.split(" "))
print("Count of words: ", len(string.split(" ")))