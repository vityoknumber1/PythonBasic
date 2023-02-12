#Рядок та зрізи

str = input("Enter a string: ")
print("String:",str)

print("Third symbol:", str[2])
print("Second last symbol:", str[-2])
print("First 5 symbols:", str[:5])
print("String except last 2 symbols:", str[:-2])
print("String with odd indexes:", str[::2])
print("String with even indexes:", str[1::2])
print("String with reverse order:", str[::-1])
print("String with reverse order through 1 symbol:", str[::-2])
print("String length:", len(str))
