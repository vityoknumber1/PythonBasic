#Завдання на словники(dictionary)

str1 = "Hello world hi hi earth hi moon hi we do we"
print("Initial string: ", str1)
words = str1.split()

dictionary = {}

for word in words:
    dictionary[word] = words.count(word)

print("Result of counting: ", dictionary)