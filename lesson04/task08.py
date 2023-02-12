#Пошук символу у рядку

s = input("Введіть рядок: ")
ch = input("Введіть символ: ")

startInd = 0
print("Індекси символу", ch, "в рядку", s, ":")

for i in range(len(s)):
    k = s.find(ch, startInd)

    if k != -1:
        startInd = k + 1
        print(k)
    else: break

if s.find(ch) == -1:
    print("Такого символу немає в рядку.")
